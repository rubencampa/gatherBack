# Generated by Django 4.0.3 on 2022-06-03 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_post_rutaimgpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rutaImgPost',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen de perfil'),
        ),
    ]
