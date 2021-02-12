# Generated by Django 3.1.6 on 2021-02-12 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_auto_20210212_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='origin_price',
            field=models.IntegerField(default=0, help_text='원래 금액'),
        ),
        migrations.AddField(
            model_name='book',
            name='origin_price',
            field=models.IntegerField(default=0, help_text='원래 금액'),
        ),
        migrations.AddField(
            model_name='etc',
            name='origin_price',
            field=models.IntegerField(default=0, help_text='원래 금액'),
        ),
        migrations.AddField(
            model_name='furniture',
            name='origin_price',
            field=models.IntegerField(default=0, help_text='원래 금액'),
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='price',
            field=models.IntegerField(default=0, help_text='판매 금액'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0, help_text='판매 금액'),
        ),
        migrations.AlterField(
            model_name='etc',
            name='price',
            field=models.IntegerField(default=0, help_text='판매 금액'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='price',
            field=models.IntegerField(default=0, help_text='판매 금액'),
        ),
    ]