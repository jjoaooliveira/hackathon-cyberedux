# Generated by Django 5.0 on 2023-12-14 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='data_abertura',
            field=models.DateField(verbose_name='data_abertura'),
        ),
    ]
