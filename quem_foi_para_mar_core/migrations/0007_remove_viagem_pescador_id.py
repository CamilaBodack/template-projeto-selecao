# Generated by Django 3.1 on 2020-08-11 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quem_foi_para_mar_core', '0006_remove_contato_pescador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viagem',
            name='pescador_id',
        ),
    ]