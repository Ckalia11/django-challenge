# Generated by Django 4.0.4 on 2022-05-27 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos_interface', '0024_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='video',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videos_interface.video'),
        ),
    ]
