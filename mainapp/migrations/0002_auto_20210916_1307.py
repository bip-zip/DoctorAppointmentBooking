# Generated by Django 3.2.7 on 2021-09-16 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctorsapp', '0001_initial'),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appliedon',
            new_name='applied_date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='appointmentdate',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='response',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Availabity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=20, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorsapp.doctor')),
            ],
            options={
                'unique_together': {('date', 'time')},
            },
        ),
    ]
