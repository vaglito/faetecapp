# Generated by Django 3.2.20 on 2023-08-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tc',
            name='tc',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]