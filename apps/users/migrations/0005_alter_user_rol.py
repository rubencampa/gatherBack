# Generated by Django 4.0.3 on 2022-05-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.IntegerField(blank=True, verbose_name='User role'),
        ),
    ]