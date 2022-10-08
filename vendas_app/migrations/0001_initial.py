# Generated by Django 4.1.2 on 2022-10-07 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=150, null=True)),
                ('preco_do_produto', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('desc', models.TextField(max_length=250)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas_app.categoria', verbose_name='Categoria')),
            ],
        ),
    ]
