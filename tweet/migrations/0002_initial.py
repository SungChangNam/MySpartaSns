# Generated by Django 4.1.1 on 2022-09-28 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tweetcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tweetcomment',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.tweetmodel'),
        ),
    ]
