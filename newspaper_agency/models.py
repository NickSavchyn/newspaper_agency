from django.conf import settings
from django.contrib.auth.models import  AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(
        verbose_name="years_of_experience",
        null=True
    )

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(
        to=Topic,
        on_delete=models.CASCADE,
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspapers"
    )

    def __str__(self):
        return self.title
