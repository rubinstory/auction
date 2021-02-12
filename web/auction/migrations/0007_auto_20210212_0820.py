# Generated by Django 3.1.6 on 2021-02-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_boardgame_etc_furniture'),
    ]

    operations = [
        migrations.AddField(
            model_name='etc',
            name='category',
            field=models.CharField(default='', help_text='물품의 종류를 입력하세요', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Freshmen', '1학년'), ('Computer', '컴퓨터공학과'), ('Electrical', '전기공학과'), ('Electric', '전자공학과'), ('Elective', '교양'), ('ETC', '기타')], default='ETC', help_text='책의 종류를 선택하세요', max_length=100),
        ),
    ]