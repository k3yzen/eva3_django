# Generated by Django 4.1.3 on 2022-11-25 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comuna",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name="Estado",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("Estado", models.CharField(max_length=35)),
            ],
        ),
        migrations.RemoveField(
            model_name="respuesta",
            name="id_consulta",
        ),
        migrations.DeleteModel(
            name="User",
        ),
        migrations.DeleteModel(
            name="Consulta",
        ),
        migrations.DeleteModel(
            name="Respuesta",
        ),
    ]
