# Generated by Django 4.2.6 on 2023-11-13 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0009_alter_imovel_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='foto',
            field=models.URLField(),
        ),
    ]
