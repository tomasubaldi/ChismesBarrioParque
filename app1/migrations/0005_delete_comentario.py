# Generated by Django 4.1.7 on 2023-04-06 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_comentario_fecha_alter_comentario_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
