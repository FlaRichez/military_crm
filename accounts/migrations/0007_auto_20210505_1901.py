# Generated by Django 3.2 on 2021-05-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210505_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='warcraft',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='warcraft',
            name='start_pose',
            field=models.DateField(auto_now=True),
        ),
    ]
