# Generated by Django 4.2.3 on 2023-08-07 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_delete_month_delete_paymentmode_delete_paymenttype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
    ]
