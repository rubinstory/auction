# Generated by Django 3.1.6 on 2021-02-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0011_auto_20210213_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='major',
            field=models.CharField(default='기타', help_text='전공을 입력하세요', max_length=100),
        ),
    ]