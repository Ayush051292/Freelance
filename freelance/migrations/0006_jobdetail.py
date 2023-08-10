# Generated by Django 4.2.3 on 2023-08-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0005_paymentobank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.CharField(max_length=255, null=True)),
                ('job_id', models.CharField(max_length=255, null=True)),
                ('words', models.IntegerField(null=True)),
                ('value', models.IntegerField(null=True)),
                ('ppw', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('currency', models.CharField(max_length=255, null=True)),
                ('value_inr', models.IntegerField(null=True)),
                ('participant', models.CharField(max_length=255, null=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(max_length=255, null=True)),
                ('updated_at', models.DateTimeField(max_length=255, null=True)),
            ],
        ),
    ]
