# Generated by Django 4.2.3 on 2023-08-09 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0009_companies_trade_license'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm_name', models.CharField(max_length=100, null=True)),
                ('crm_number', models.CharField(max_length=100, null=True)),
                ('per_word_rate_mother', models.CharField(max_length=100, null=True)),
                ('per_word_rate_inr', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('credit_limt', models.CharField(max_length=100, null=True)),
                ('gst', models.CharField(max_length=100, null=True)),
                ('tds', models.CharField(max_length=100, null=True)),
                ('inv_email', models.CharField(max_length=100, null=True)),
                ('contact_email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.paymentobank')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.currencies')),
                ('payment_mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.paymentmode')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.paymenttype')),
            ],
        ),
    ]
