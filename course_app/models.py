from django.db import models
from pytils.translit import slugify


class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField("description")
    slug = models.SlugField(max_length=200, unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Choose course"
    )
    theme = models.CharField(
        "Lesson theme",
        max_length=200,
    )
    content = models.TextField("description", blank=True, null=True)
    youtube_url = models.CharField("Youtubeurl", max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.course.name} - {self.theme}"
