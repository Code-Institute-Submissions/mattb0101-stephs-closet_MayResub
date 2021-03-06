# Generated by Django 3.1.6 on 2021-02-28 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20210225_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockTransactions',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('product', models.ForeignKey(
                    max_length=254,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='transaction', to='stock.stock')),
            ],
        ),
    ]
