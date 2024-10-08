# Generated by Django 5.0.6 on 2024-09-13 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('po_box', models.CharField(blank=True, max_length=100, null=True)),
                ('emergency_phone_number', models.CharField(max_length=15)),
                ('passport_number', models.CharField(max_length=20)),
                ('visa_document', models.FileField(blank=True, null=True, upload_to='visas/')),
                ('departure_city', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
            ],
        ),
    ]
