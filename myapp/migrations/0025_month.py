# Generated by Django 4.2.3 on 2023-08-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_delete_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=255)),
                ('created_at', models.CharField(max_length=255, null=True)),
                ('updated_at', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
