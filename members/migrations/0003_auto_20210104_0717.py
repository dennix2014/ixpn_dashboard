# Generated by Django 3.0.7 on 2021-01-04 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20210103_0754'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['short_name']},
        ),
        migrations.AlterModelOptions(
            name='portconnection',
            options={'ordering': ['member_name']},
        ),
    ]
