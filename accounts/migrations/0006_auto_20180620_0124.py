# Generated by Django 2.0.6 on 2018-06-20 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180620_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='no-img.jpg', upload_to='assets/images'),
        ),
    ]
