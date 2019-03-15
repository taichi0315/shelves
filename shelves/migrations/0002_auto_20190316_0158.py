# Generated by Django 2.1.5 on 2019-03-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='recommend_user_list',
            field=models.TextField(default=',', verbose_name='おすすめユーザーリスト'),
        ),
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.TextField(blank=True, verbose_name='コメント'),
        ),
    ]
