# Generated by Django 3.1.6 on 2021-02-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_book_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, help_text='책의 이미지를 업로드하세요', null=True, upload_to='images/books'),
        ),
    ]