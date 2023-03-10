# Generated by Django 3.2.16 on 2022-12-08 12:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("name",),
                "verbose_name": ("Категория",),
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ("-pub_date",),
                "verbose_name": ("Комментарий",),
                "verbose_name_plural": "Комментарии",
            },
        ),
        migrations.AlterModelOptions(
            name="genre",
            options={
                "ordering": ("name",),
                "verbose_name": ("Жанр",),
                "verbose_name_plural": "Жанры",
            },
        ),
        migrations.AlterModelOptions(
            name="review",
            options={
                "ordering": ("-pub_date",),
                "verbose_name": ("Отзыв",),
                "verbose_name_plural": "Отзывы",
            },
        ),
        migrations.AlterModelOptions(
            name="title",
            options={
                "ordering": ("name",),
                "verbose_name": ("Произведение",),
                "verbose_name_plural": "Произведения",
            },
        ),
        migrations.AlterField(
            model_name="review",
            name="score",
            field=models.PositiveSmallIntegerField(
                default=5,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(10),
                ],
                verbose_name="Оценка произведения (1-10)",
            ),
        ),
    ]
