from django.db import models

# Create your models here.
class Province(models.Model):
    title = models.CharField(
        max_length=32,
        unique=True,
    )

    def __str__(self):
        return self.title

class City(models.Model):
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name='cities',
    )
    title = models.CharField(
        max_length=64,
    )
    slug = models.SlugField(
        max_length=64,
        unique=True,
    )

    class Meta:
        ordering = [
            'title'
        ]
        indexes = [
            models.Index(fields=['title']),
        ]
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.title

class Neighborhood(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='neighborhoods',
    )
    title = models.CharField(
        max_length=64,
    )

    class Meta:
        ordering = [
            'title'
        ]
        indexes = [
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title
