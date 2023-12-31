# Generated by Django 4.2.3 on 2023-08-25 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('travel_service', '0001_initial'),
        ('news', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0001_initial'),
        ('favorite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistalbum',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='housefavorite',
            name='housing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.housing'),
        ),
        migrations.AddField(
            model_name='housefavorite',
            name='news',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.news'),
        ),
        migrations.AddField(
            model_name='housefavorite',
            name='transfer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travel_service.transfer'),
        ),
        migrations.AddField(
            model_name='housefavorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='housefavorite',
            name='wishlist_album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='favorite.wishlistalbum'),
        ),
    ]
