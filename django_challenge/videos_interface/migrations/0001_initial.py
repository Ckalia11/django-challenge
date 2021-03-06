# Generated by Django 4.0.4 on 2022-05-07 15:10

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('comments', models.TextField()),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]
