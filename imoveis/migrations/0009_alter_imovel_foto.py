# Generated by Django 4.2.6 on 2023-11-13 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0008_alter_imovel_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='imagens'),
        ),
    ]
