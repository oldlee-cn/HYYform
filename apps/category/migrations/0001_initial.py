# Generated by Django 2.0 on 2019-05-13 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
                ('desc', models.TextField(max_length=200, verbose_name='描述')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '报修分类',
                'verbose_name_plural': '报修分类',
            },
        ),
    ]
