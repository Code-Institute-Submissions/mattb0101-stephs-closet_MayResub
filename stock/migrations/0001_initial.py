# Generated by Django 3.1.6 on 2021-02-20 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0007_auto_20210216_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('in_stock', models.IntegerField(blank=True, default=0)),
                ('product', models.ForeignKey(
                    max_length=254,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='products.product')),
            ],
        ),
    ]
