# Generated by Django 3.0.5 on 2020-12-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201214_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='yamdbuser',
            name='bio',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='yamdbuser',
            name='role',
            field=models.CharField(blank=True, choices=[('user', 'User'), ('moderator', 'Moderator'), ('admin', 'Admin')], default='user', max_length=15, verbose_name='Роль пользователя'),
        ),
    ]