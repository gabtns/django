# Generated by Django 4.1.3 on 2023-08-06 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("web_2", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="modelos",
            name="published",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="FECHA DE PUBLICACIÓN"
            ),
        ),
    ]
