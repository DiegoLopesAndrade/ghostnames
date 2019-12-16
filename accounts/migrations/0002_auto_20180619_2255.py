# Generated by Django 2.0.6 on 2018-06-19 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='none@email.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
