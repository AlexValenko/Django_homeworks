from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=100, verbose_name="Заголовок", unique=True, help_text="Заголовок статьи")
    content = models.TextField(null=True, blank=True, verbose_name="Содержимое", help_text="Текст статьи")
    preview = models.ImageField(upload_to="previews/", verbose_name="Превью", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    is_published = models.BooleanField(
        null=False, default=False, blank=False, verbose_name="Признак публикации", help_text="Статья опубликована?"
    )
    views_counter = models.PositiveIntegerField(verbose_name="Счетчик просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = [
            "created_at",
        ]
