# Generated by Django 2.1 on 2019-10-12 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='邮箱'),
        ),
    ]
