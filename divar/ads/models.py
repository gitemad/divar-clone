from django.db import (
    models,
    transaction,
)
from django.contrib.auth import get_user_model
from django.contrib.postgres.indexes import GinIndex
from django.core.exceptions import ValidationError
import uuid
from location.models import (
    City,
    Neighborhood,
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

class Advertise(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(
        max_length=256,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='advertises',
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='advertises',
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='advertises',
    )
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.CASCADE,
        related_name='advertises',
        null=True,
        blank=True,
    )
    description = models.TextField()
    image = models.ImageField(
        null=True,
        blank=True,
    )
    price = models.PositiveBigIntegerField()
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            '-created'
        ]
        indexes = [
            models.Index(fields=['-created']),
            GinIndex(
                name='idx_advertise_title_gin',
                fields=['title'],
                opclasses=['gin_trgm_ops'],
            ),
        ]
    
    def clean(self):
        super().clean()
        if self.neighborhood:
            if self.neighborhood.city != self.city:
                raise ValidationError("Neighborhood must belong to the selected city.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.user}'
