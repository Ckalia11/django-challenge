# Generated by Django 4.0.4 on 2022-05-09 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos_interface', '0006_user_rename_comment_video_comments_remove_video_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='comments',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos_interface.user')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='comment_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='videos_interface.comment'),
        ),
    ]
