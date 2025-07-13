from django.db import (
    models,
    transaction,
)

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=64,
    )
    slug = models.SlugField(
        max_length=64,
        unique=True,
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
    )
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = [
            'order'
        ]
        unique_together = (
            'parent',
            'order',
        )
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if self.pk:
            original = Category.objects.get(pk=self.pk)
            previous_order = original.order
            self._reorder(previous_order)
        else:
            max_order = Category.objects.filter(parent=self.parent)\
                .aggregate(order_max=models.Max('order'))['order_max']

            self.order = (max_order or 0) + 1

        super().save(*args, **kwargs)

    def _reorder(self, previous_order):
        new_order = self.order

        with transaction.atomic():
            if new_order < previous_order:
                Category.objects.filter(parent=self.parent, order__gte=new_order, order__lt=previous_order)\
                    .update(order=models.F('order') + 1)
            else:
                Category.objects.filter(parent=self.parent, order__gt=previous_order, order__lte=new_order)\
                    .update(order=models.F('order') - 1)

            Category.objects.filter(pk=self.pk).update(order=new_order)

    def __str__(self):
        return self.title
