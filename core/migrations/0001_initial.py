# Generated by Django 2.2.5 on 2020-03-16 23:20
#Uma migration inicial
#A partir dessa migration vai ser criado um banco de dados
#Cada migration representa o historico de modelagem de banco de dados
#Podendo utilizar versões diferentes de migrations se for o caso
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
    #Criando um modelo 
    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Quantidade em Estoque')),
            ],
        ),
    ]
