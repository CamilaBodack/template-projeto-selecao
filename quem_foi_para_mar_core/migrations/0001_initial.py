# Generated by Django 3.1 on 2020-08-11 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=254, verbose_name='Endereço')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=50, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Embarcacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome')),
                ('numeracao', models.CharField(max_length=50, verbose_name='Numeração')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo')),
                ('caracteristicas', models.CharField(max_length=254, verbose_name='características')),
            ],
        ),
        migrations.CreateModel(
            name='Pescador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=254, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=50, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=254, verbose_name='Destino')),
                ('data_partida', models.DateField(verbose_name='Data de partida')),
                ('data_chegada_prevista', models.DateField(verbose_name='Data de chegada prevista')),
                ('tripulacao', models.CharField(max_length=254, verbose_name='Nome dos tripulantes')),
                ('embarcacao_retornou', models.BooleanField(default=False, verbose_name='Retornou ?')),
                ('embarcacao_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quem_foi_para_mar_core.embarcacao')),
                ('pescador_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quem_foi_para_mar_core.pescador')),
            ],
        ),
    ]