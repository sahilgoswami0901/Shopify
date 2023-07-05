# Generated by Django 3.1.5 on 2023-03-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(max_length=100)),
                ('Customer_Address', models.CharField(max_length=200)),
                ('Customer_Email', models.CharField(max_length=100)),
                ('Customer_Phone_no', models.BigIntegerField()),
                ('Date_of_Birth', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
            ],
        ),
    ]
