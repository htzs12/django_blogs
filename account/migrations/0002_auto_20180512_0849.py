# Generated by Django 2.0.2 on 2018-05-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='images/touxiang.jpg', upload_to='images/%Y/%m', verbose_name='头像'),
        ),
    ]