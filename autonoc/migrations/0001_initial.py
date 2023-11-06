# Generated by Django 4.2.6 on 2023-11-06 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CanalVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Canais de Vendas',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('sigla', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=128)),
                ('nome', models.CharField(max_length=128)),
                ('cnpj', models.CharField(max_length=128)),
                ('logradouro', models.CharField(max_length=128)),
                ('numero', models.CharField(max_length=128)),
                ('bairro', models.CharField(max_length=128)),
                ('cep', models.CharField(max_length=128)),
                ('telefone', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.cidade')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Conexao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.IntegerField()),
                ('logradouro_instalacao', models.CharField(max_length=128)),
                ('banda_contrato', models.IntegerField()),
                ('data_contrato', models.DateField()),
                ('data_ativacao', models.DateField()),
                ('data_vencimento', models.DateField()),
                ('observacao', models.TextField()),
                ('sinal', models.BooleanField(default=True)),
                ('banda_reducao', models.IntegerField()),
                ('canal_venda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.canalvenda')),
                ('cidade_instalacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.cidade')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.cliente')),
            ],
            options={
                'verbose_name_plural': 'Conexões',
            },
        ),
        migrations.CreateModel(
            name='Consultor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('telefone', models.CharField(max_length=128)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Consultores',
            },
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('modelo', models.CharField(max_length=128)),
                ('ip', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Equipamentos',
            },
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Formas de Pagamento',
            },
        ),
        migrations.CreateModel(
            name='Operacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Operações',
            },
        ),
        migrations.CreateModel(
            name='ServicoContrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Serviços do Contrato',
            },
        ),
        migrations.CreateModel(
            name='StatusContrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='nome *')),
                ('observacao', models.TextField(max_length=512)),
            ],
            options={
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Vlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_vlan', models.IntegerField(help_text='valor entre 1 á 4094')),
                ('nome', models.CharField(help_text='nome deve ser único', max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'VLANs',
            },
        ),
        migrations.CreateModel(
            name='FinanceiroCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_a_pagar', models.FloatField()),
                ('data_debito', models.DateField()),
                ('mes_debito', models.CharField(blank=True, max_length=64, null=True)),
                ('ano_debito', models.IntegerField(blank=True, null=True)),
                ('conexao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.conexao')),
                ('forma_de_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.formapagamento')),
            ],
        ),
        migrations.CreateModel(
            name='Faturamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('vencimento', models.DateField()),
                ('valor_faturado', models.FloatField()),
                ('valor_recebido', models.FloatField()),
                ('saldo', models.FloatField()),
                ('data_pagamento', models.DateField()),
                ('nf', models.IntegerField()),
                ('data_nf', models.DateField()),
                ('data_envio_nf', models.DateField()),
                ('mes_vencimento', models.CharField(blank=True, max_length=64, null=True)),
                ('ano_vencimento', models.IntegerField(blank=True, null=True)),
                ('conexao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.conexao')),
            ],
            options={
                'verbose_name_plural': 'Faturamentos',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('uf', models.CharField(max_length=2)),
                ('operacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.operacao')),
            ],
            options={
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Estacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('logradouro', models.CharField(max_length=128)),
                ('numero', models.CharField(max_length=128)),
                ('bairro', models.CharField(max_length=128)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.cidade')),
            ],
            options={
                'verbose_name_plural': 'Estações',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=128)),
                ('nome', models.CharField(max_length=128)),
                ('cnpj', models.CharField(max_length=128)),
                ('logradouro', models.CharField(max_length=128)),
                ('numero', models.CharField(max_length=128)),
                ('bairro', models.CharField(max_length=128)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.cidade')),
            ],
            options={
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.AddField(
            model_name='conexao',
            name='consultor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.consultor'),
        ),
        migrations.AddField(
            model_name='conexao',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.empresa'),
        ),
        migrations.AddField(
            model_name='conexao',
            name='operacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.operacao'),
        ),
        migrations.AddField(
            model_name='conexao',
            name='servico_contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.servicocontrato'),
        ),
        migrations.AddField(
            model_name='conexao',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.statuscontrato'),
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
                ('id_vlan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.vlan')),
            ],
            options={
                'verbose_name_plural': 'Circuitos',
            },
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autonoc.estado'),
        ),
    ]
