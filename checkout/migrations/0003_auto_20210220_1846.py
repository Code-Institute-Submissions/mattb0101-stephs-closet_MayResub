# Generated by Django 3.1.6 on 2021-02-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210219_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_size',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
