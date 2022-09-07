# Generated by Django 4.1.1 on 2022-09-05 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('modify_time', models.DateTimeField(auto_now=True, help_text='修改时间')),
                ('title', models.CharField(help_text='主题', max_length=200)),
                ('content', models.TextField(help_text='内容')),
                ('user', models.ForeignKey(help_text='关联用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('modify_time', models.DateTimeField(auto_now=True, help_text='修改时间')),
                ('comment', models.TextField(help_text='评论')),
                ('up', models.IntegerField(default=0, help_text='支持')),
                ('down', models.IntegerField(default=0, help_text='反对')),
                ('topic', models.ForeignKey(help_text='关联主题', on_delete=django.db.models.deletion.CASCADE, to='blog.topic')),
                ('user', models.ForeignKey(help_text='关联用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_time'],
                'abstract': False,
            },
        ),
    ]