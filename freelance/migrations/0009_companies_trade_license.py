# Generated by Django 4.2.3 on 2023-08-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0008_companies_email_companies_phone_companies_regno'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='trade_license',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
