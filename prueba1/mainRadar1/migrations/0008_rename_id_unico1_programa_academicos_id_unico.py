# Generated by Django 4.2.7 on 2023-11-04 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainRadar1', '0007_alter_comentario_id_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programa_academicos',
            old_name='id_unico1',
            new_name='id_unico',
        ),
    ]
