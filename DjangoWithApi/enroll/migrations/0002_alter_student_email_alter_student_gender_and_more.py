# Generated by Django 5.0.2 on 2024-05-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]