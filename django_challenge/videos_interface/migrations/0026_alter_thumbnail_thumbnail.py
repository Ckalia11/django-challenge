# Generated by Django 4.0.4 on 2022-05-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_interface', '0025_thumbnail_thumbnail_alter_thumbnail_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name=''),
        ),
    ]