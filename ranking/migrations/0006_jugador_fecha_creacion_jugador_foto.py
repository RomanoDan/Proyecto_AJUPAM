# Generated by Django 5.1.5 on 2025-02-25 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0005_alter_jugador_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='fecha_creacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jugador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
