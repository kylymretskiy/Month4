from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    DEGREE_CHOICES = (
        ("bachelor", "Бакалавр"),
        ("master", "Магистр"),
        ("docent", "Доцент"),
        ("none", "Без диплома"),
    )

    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES, default="none")
    gender = models.CharField(max_length=10, choices=GENDER, default="Male")
    age = models.PositiveIntegerField(default=7)
    phone_number = models.CharField(max_length=20)
    position = models.CharField(max_length=100, blank=True, null=True)
    salary = models.PositiveIntegerField(blank=True, null=True)
    experience = models.PositiveIntegerField(default=0)
    skills = models.TextField(blank=True)
    languages = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if self.degree == "bachelor":
            self.position = "Библиотекарь"
            self.salary = 20000
        elif self.degree == "master":
            self.position = "Главный библиотекарь"
            self.salary = 40000
        elif self.degree == "docent":
            self.position = "Директор"
            self.salary = 60000
        else:
            self.position = "уборщица"
            self.salary = 17000

        super().save(*args, **kwargs)
