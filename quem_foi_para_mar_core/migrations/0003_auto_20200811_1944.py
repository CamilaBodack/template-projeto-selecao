# Generated by Django 3.1 on 2020-08-11 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quem_foi_para_mar_core', '0002_contato_pescador_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='pescador_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='quem_foi_para_mar_core.pescador'),
        ),
    ]