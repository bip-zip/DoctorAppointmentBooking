# Generated by Django 3.2.7 on 2021-09-16 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorName', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('pathologist', 'Pathologist'), ('psychiatrist', 'Psychiatrist'), ('surgeon', 'Surgeon'), ('anesthesiologist', 'Anesthesilogist'), ('neurologist', 'Neurologist'), ('pulmonologist', 'Pulmonologist'), ('dermatologist', 'Dermatologist'), ('cardiologist', 'Cardiologist')], max_length=200)),
                ('age', models.IntegerField()),
                ('number', models.CharField(max_length=12)),
                ('picture', models.ImageField(upload_to='doctor_profile')),
                ('time', models.CharField(max_length=12)),
            ],
        ),
    ]
