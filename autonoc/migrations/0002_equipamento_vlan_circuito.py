# Generated by Django 4.2.6 on 2023-10-26 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autonoc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('modelo', models.CharField(max_length=128)),
                ('serial', models.CharField(max_length=128)),
                ('mac', models.CharField(max_length=128)),
                ('ip', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Equipamentos',
            },
        ),
        migrations.CreateModel(
            name='Vlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'VLANs',
            },
        ),
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponta_a', models.CharField(max_length=128)),
                ('ponta_b', models.CharField(max_length=128)),
                ('id_sensor_prtg', models.IntegerField()),
                ('designacao', models.CharField(max_length=128, unique=True)),
                ('rack', models.CharField(max_length=128)),
                ('fila', models.CharField(max_length=128)),
                ('porta', models.CharField(max_length=128)),
                ('ip_circuito', models.CharField(max_length=128)),
                ('submask', models.IntegerField()),
                ('dgo_cto', models.CharField(max_length=128)),
                ('porta_dgo_cto', models.IntegerField()),
                ('conexao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.conexao')),
                ('equipamento_acesso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='circuito_acesso', to='autonoc.equipamento')),
                ('equipamento_ultima_milha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='circuito_ultima_milha', to='autonoc.equipamento')),
                ('estacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.estacao')),
                ('vlan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.vlan')),
            ],
            options={
                'verbose_name_plural': 'Circuitos',
            },
        ),
    ]
