# Generated by Django 4.2.14 on 2024-07-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0003_subscribe"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="amount",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Цена"
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="amount",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Цена"
            ),
        ),
    ]
