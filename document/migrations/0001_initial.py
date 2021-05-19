# Generated by Django 3.2 on 2021-04-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('data_created', models.DateField(auto_now_add=True)),
                ('data_expired', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('dead', 'dead')], max_length=50)),
                ('document_root', models.CharField(choices=[('public', 'public'), ('private', 'private'), ('secret', 'secret'), ('top-secret', 'top-secret')], max_length=50)),
            ],
        ),
    ]