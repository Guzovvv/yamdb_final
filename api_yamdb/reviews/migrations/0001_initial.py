# Generated by Django 2.2.16 on 2022-05-09 10:47

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="Имя пользователя"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Почта"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=150, verbose_name="Имя"),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Фамилия"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("user", "user"),
                            ("moderator", "moderator"),
                            ("admin", "admin"),
                        ],
                        default="user",
                        max_length=50,
                        verbose_name="Роль пользователя",
                    ),
                ),
                (
                    "bio",
                    models.TextField(blank=True, verbose_name="Биография пользователя"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
                "ordering": ["username"],
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=256, unique=True, verbose_name="Категория"
                    ),
                ),
                ("slug", models.SlugField(unique=True, verbose_name="Адрес")),
            ],
            options={
                "verbose_name": ("Категория",),
                "verbose_name_plural": "Категории",
                "ordering": (["name"],),
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, unique=True, verbose_name="Жанр"),
                ),
                ("slug", models.SlugField(unique=True, verbose_name="Адрес")),
            ],
            options={
                "verbose_name": ("Жанр",),
                "verbose_name_plural": "Жанры",
                "ordering": (["name"],),
            },
        ),
        migrations.CreateModel(
            name="Title",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=256, verbose_name="Название произведения"
                    ),
                ),
                (
                    "year",
                    models.PositiveSmallIntegerField(
                        db_index=True,
                        default=2022,
                        validators=[django.core.validators.MaxValueValidator(2022)],
                        verbose_name="Дата создания произведения",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        null=True,
                        verbose_name="Описание произведения",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="titles",
                        to="reviews.Category",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "genre",
                    models.ManyToManyField(
                        default=None, null=True, to="reviews.Genre", verbose_name="Жанр"
                    ),
                ),
            ],
            options={
                "verbose_name": ("Произведение",),
                "verbose_name_plural": "Произведения",
                "ordering": (["name"],),
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Текст отзыва")),
                (
                    "score",
                    models.IntegerField(
                        default=5,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ],
                        verbose_name="Оценка произведения (1-10)",
                    ),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name="Дата публикации отзыва",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор отзыва",
                    ),
                ),
                (
                    "title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="reviews.Title",
                        verbose_name="Произведение",
                    ),
                ),
            ],
            options={
                "verbose_name": ("Отзыв",),
                "verbose_name_plural": "Отзывы",
                "ordering": ["-pub_date"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Текст комментария")),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name="Дата добавления комментария",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор комментария",
                    ),
                ),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="reviews.Review",
                        verbose_name="Отзыв",
                    ),
                ),
                (
                    "title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="reviews.Title",
                        verbose_name="Произведение",
                    ),
                ),
            ],
            options={
                "verbose_name": ("Комментарий",),
                "verbose_name_plural": "Комментарии",
                "ordering": ["-pub_date"],
            },
        ),
        migrations.AddConstraint(
            model_name="title",
            constraint=models.UniqueConstraint(
                fields=("name", "year", "category"), name="unique_title"
            ),
        ),
        migrations.AddConstraint(
            model_name="review",
            constraint=models.UniqueConstraint(
                fields=("title", "author"), name="unique_review"
            ),
        ),
    ]
