# Generated by Django 4.0.3 on 2022-05-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_tema_tipopost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tema',
            field=models.IntegerField(verbose_name='Tema Post'),
        ),
    ]
