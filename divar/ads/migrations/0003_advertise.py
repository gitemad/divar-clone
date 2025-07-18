# Generated by Django 5.2.3 on 2025-07-15 16:55

import django.contrib.postgres.indexes
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_enable_pg_trgm_extension'),
        ('location', '0002_alter_city_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.PositiveBigIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertises', to='ads.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertises', to='location.city')),
                ('neighborhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertises', to='location.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertises', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-created'], name='ads_adverti_created_a441cc_idx'), django.contrib.postgres.indexes.GinIndex(fields=['title'], name='idx_advertise_title_gin', opclasses=['gin_trgm_ops'])],
            },
        ),
    ]
