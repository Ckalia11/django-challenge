# Generated by Django 4.0.4 on 2022-06-06 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_interface', '0029_alter_thumbnail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(default=1, upload_to='videos/', verbose_name=''),
            preserve_default=False,
        ),
    ]
