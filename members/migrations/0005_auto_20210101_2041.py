# Generated by Django 3.0.7 on 2021-01-01 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_aka_switch_switchport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switchport',
            name='switch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='swichy', to='members.Switch'),
        ),
    ]