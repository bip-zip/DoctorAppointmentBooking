# Generated by Django 3.2.7 on 2021-09-16 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctorsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phonenumber', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=20, null=True)),
                ('desc', models.TextField(null=True)),
                ('seen', models.BooleanField(default=False)),
                ('response', models.CharField(blank=True, max_length=500, null=True)),
                ('appointmentdate', models.CharField(max_length=20, null=True)),
                ('appliedon', models.DateField(auto_now_add=True, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctorsapp.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
