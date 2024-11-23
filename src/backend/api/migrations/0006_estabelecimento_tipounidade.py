# Generated by Django 5.1 on 2024-11-23 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_delete_indicator_alter_cidade_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('codigo_cnes', models.IntegerField(primary_key=True, serialize=False)),
                ('nome_fantasia', models.CharField(max_length=255)),
                ('endereco_estabelecimento', models.CharField(max_length=255)),
                ('numero_estabelecimento', models.CharField(max_length=10)),
                ('bairro_estabelecimento', models.CharField(max_length=255)),
                ('codigo_cep_estabelecimento', models.CharField(max_length=10)),
                ('latitude_estabelecimento_decimo_grau', models.FloatField()),
                ('longitude_estabelecimento_decimo_grau', models.FloatField()),
                ('numero_telefone_estabelecimento', models.CharField(max_length=20, null=True)),
                ('descricao_turno_atendimento', models.CharField(max_length=255)),
                ('estabelecimento_faz_atendimento_ambulatorial_sus', models.CharField(max_length=3)),
                ('estabelecimento_possui_centro_cirurgico', models.IntegerField()),
                ('estabelecimento_possui_servico_apoio', models.IntegerField()),
                ('estabelecimento_possui_atendimento_ambulatorial', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoUnidade',
            fields=[
                ('codigo_tipo_unidade', models.IntegerField(primary_key=True, serialize=False)),
                ('descricao_tipo_unidade', models.CharField(max_length=255)),
            ],
        ),
    ]
