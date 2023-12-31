# Generated by Django 4.2.5 on 2023-09-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="description",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="movie",
            name="name",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="active",
            field=models.BooleanField(default=True, null=True),
        ),
    ]
