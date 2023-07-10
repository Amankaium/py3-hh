from django.db import models
from worker.models import Worker


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='Нет описания')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    candidate = models.ManyToManyField(
        to=Worker,
        blank=True,
    )
    category = models.ForeignKey(
        to='Category',
        null=True,  # обязательный в базе данных
        blank=True,  # обязательный в django
        on_delete=models.SET_NULL,
        verbose_name='категория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['salary']
        unique_together = [['title', 'email']]


class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateField()
    workers = models.ManyToManyField(
        to=Worker,
        blank=True,
        related_name='company',
    )

    def __str__(self):
        return self.name

