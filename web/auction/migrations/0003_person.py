# Generated by Django 3.1.6 on 2021-02-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auto_20210211_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='이름을 입력하세요', max_length=100)),
                ('major', models.CharField(choices=[('CSE', '정보컴퓨터공학과'), ('EEC', '전기공학과'), ('EE', '전자공학과'), ('ETC', '기타')], default='ETC', help_text='전공을 선택하세요', max_length=100)),
                ('student_id', models.CharField(default='', help_text='학번을 입력하세요', max_length=100)),
            ],
        ),
    ]
