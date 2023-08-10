# Generated by Django 4.2.3 on 2023-08-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_companies_currencies_month_delete_paymentmode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paymentmode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(max_length=255)),
                ('p_order', models.CharField(max_length=255, null=True)),
                ('max_allocation', models.CharField(max_length=255, null=True)),
                ('display_name', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(max_length=255)),
                ('updated_at', models.DateTimeField(max_length=255)),
            ],
        ),
    ]
