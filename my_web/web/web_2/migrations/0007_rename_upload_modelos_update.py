# Generated by Django 4.1.3 on 2023-08-09 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web_2", "0006_modelos_url_alter_modelos_imagen"),
    ]

    operations = [
        migrations.RenameField(
            model_name="modelos", old_name="upload", new_name="update",
        ),
    ]
