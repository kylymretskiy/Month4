from django.db import models

class Books(models.Model):
    GENRE=(
        ("Ужасы","Ужасы"),
        ("Комедия","Комедия"),
    )
    image = models.ImageField(upload_to='books/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=10, choices=GENRE )
    email = models.EmailField()
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.title