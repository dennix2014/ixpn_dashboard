# Generated by Django 3.0.7 on 2021-01-02 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20210101_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aka',
            name='pot',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='members.SwitchPort'),
        ),
    ]