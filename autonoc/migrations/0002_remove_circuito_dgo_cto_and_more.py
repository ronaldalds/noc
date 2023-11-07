# Generated by Django 4.2.6 on 2023-11-07 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autonoc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circuito',
            name='dgo_cto',
        ),
        migrations.RemoveField(
            model_name='circuito',
            name='equipamento_acesso',
        ),
        migrations.RemoveField(
            model_name='circuito',
            name='equipamento_ultima_milha',
        ),
        migrations.RemoveField(
            model_name='circuito',
            name='estacao',
        ),
        migrations.RemoveField(
            model_name='circuito',
            name='fila',
        ),
        migrations.RemoveField(
            model_name='circuito',
            name='porta',
        ),
        migrations.RemoveField(
            model_name='circuito',
            name='porta_dgo_cto',
        ),
        migrations.RemoveField(
            model_name='circuito',
            name='rack',
        ),
        migrations.AddField(
            model_name='circuito',
            name='interface_ponta_a',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circuito',
            name='interface_ponta_b',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='nome_fantasia',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipamento',
            name='estacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='autonoc.estacao'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipamento',
            name='fila',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='rack',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='circuito',
            name='ponta_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='circuito_ponta_a', to='autonoc.equipamento'),
        ),
        migrations.AlterField(
            model_name='circuito',
            name='ponta_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='circuito_ponta_b', to='autonoc.equipamento'),
        ),
        migrations.AlterField(
            model_name='circuito',
            name='submask',
            field=models.IntegerField(help_text='valor entre 0 á 32'),
        ),
    ]
