# Generated by Django 4.2.3 on 2023-08-09 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0011_rename_department_crm_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crm',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.companies'),
        ),
    ]
