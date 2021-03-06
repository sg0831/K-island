# Generated by Django 3.2.8 on 2021-10-22 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='like',
            new_name='likes',
        ),
        migrations.RemoveField(
            model_name='music',
            name='youtube_views',
        ),
        migrations.AlterField(
            model_name='playlist',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='LikeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.playlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
