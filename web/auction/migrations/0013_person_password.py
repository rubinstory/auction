# Generated by Django 3.1.6 on 2021-02-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0012_auto_20210213_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default='password', help_text='비밀번호를 입력하세요', max_length=100),
        ),
    ]
