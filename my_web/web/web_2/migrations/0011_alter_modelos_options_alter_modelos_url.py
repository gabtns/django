# Generated by Django 4.1.3 on 2023-08-19 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_2", "0010_alter_modelos_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="modelos",
            options={
                "ordering": ["-created"],
                "verbose_name": "Modelo",
                "verbose_name_plural": "Modelos",
            },
        ),
        migrations.AlterField(
            model_name="modelos",
            name="url",
            field=models.URLField(blank=True, verbose_name="url"),
        ),
    ]
