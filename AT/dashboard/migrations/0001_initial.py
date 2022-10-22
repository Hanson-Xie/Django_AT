# Generated by Django 4.1.1 on 2022-10-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, db_column='Date', db_tablespace='Currencies', null=True)),
                ('product', models.CharField(db_column='Material_name', db_tablespace='Currencies', max_length=255)),
                ('price', models.DecimalField(blank=True, db_column='Price', db_tablespace='Currencies', decimal_places=2, max_digits=20, null=True)),
            ],
            options={
                'db_table': 'Currencies',
                'ordering': ('product',),
            },
        ),
        migrations.CreateModel(
            name='Currency_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(db_column='Product', db_tablespace='Currencies_table', max_length=255)),
                ('date', models.DateField(blank=True, db_column='Date', db_tablespace='Currencies_table', null=True)),
                ('price', models.DecimalField(blank=True, db_column='Price', db_tablespace='Currencies_table', decimal_places=2, max_digits=20, null=True)),
                ('day', models.CharField(db_column='Day', db_tablespace='Currencies_table', max_length=255)),
                ('week', models.CharField(db_column='Week', db_tablespace='Currencies_table', max_length=255)),
                ('month', models.CharField(db_column='Month', db_tablespace='Currencies_table', max_length=255)),
                ('quarter', models.CharField(db_column='Quarter', db_tablespace='Currencies_table', max_length=255)),
                ('year', models.CharField(db_column='Year', db_tablespace='Currencies_table', max_length=255)),
            ],
            options={
                'db_table': 'Currencies_table',
                'ordering': ('product',),
            },
        ),
    ]