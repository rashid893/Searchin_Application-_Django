# Generated by Django 3.2.8 on 2021-10-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companyclass',
            fields=[
                ('jobid', models.CharField(max_length=100)),
                ('jobprofile', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('employid', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
