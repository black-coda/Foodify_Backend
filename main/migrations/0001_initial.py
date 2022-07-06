# Generated by Django 4.0.6 on 2022-07-09 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CafetriaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafeteria', models.CharField(choices=[('cafe 1', 'Anchor Cafteria 1'), ('Cafe 2', 'Anchor Cafeteria 2')], max_length=20)),
            ],
            options={
                'verbose_name': 'Cafeteria',
                'verbose_name_plural': 'Cafeterias',
            },
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Food Category',
            },
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('name_of_food', models.CharField(max_length=200)),
                ('price', models.CharField(blank=True, default='All food are minimum of N100', max_length=200, null=True)),
                ('available', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cafetria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.cafetriatype')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.foodcategory')),
            ],
            options={
                'ordering': ('name_of_food',),
            },
        ),
    ]
