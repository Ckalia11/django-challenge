# Generated by Django 4.0.4 on 2022-05-27 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos_interface', '0023_alter_video_clicks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thumbnail_video', to='videos_interface.video')),
            ],
        ),
    ]
