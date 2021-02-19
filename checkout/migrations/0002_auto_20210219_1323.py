# Generated by Django 3.1.6 on 2021-02-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='lineitem_subtotal',
            new_name='lineitem_total',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='product_size',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
