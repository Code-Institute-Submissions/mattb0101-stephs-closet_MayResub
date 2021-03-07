# Generated by Django 3.1.6 on 2021-02-21 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20210221_1239'),
        ('checkout', '0004_auto_20210221_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='orders', to='profile.useraccount'),
        ),
    ]
