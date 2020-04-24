# Generated by Django 3.0.5 on 2020-04-24 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='header_img', verbose_name='Imagem')),
                ('tituloGrande', models.CharField(max_length=100, verbose_name='Título Grande')),
                ('whatsapp', models.CharField(max_length=100, verbose_name='Link Whatsapp')),
            ],
            options={
                'verbose_name': 'Header',
                'verbose_name_plural': 'Headers',
            },
        ),
    ]
