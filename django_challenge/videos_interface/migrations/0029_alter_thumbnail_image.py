# Generated by Django 4.0.4 on 2022-05-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_interface', '0028_thumbnail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name=''),
        ),
    ]
