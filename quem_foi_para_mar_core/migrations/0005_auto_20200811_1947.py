# Generated by Django 3.1 on 2020-08-11 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quem_foi_para_mar_core', '0004_auto_20200811_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='pescador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quem_foi_para_mar_core.pescador'),
        ),
    ]