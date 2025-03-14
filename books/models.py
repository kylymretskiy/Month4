from django.db import models

class Books(models.Model):
    GENRE=(
        ("Ужасы","Ужасы"),
        ("Комедия","Комедия"),
    )
    image = models.ImageField(upload_to='books/',verbose_name = 'загрузите фото', null=True )
    title = models.CharField(max_length=100,verbose_name = 'укажите название книги', null=True)
    description = models.TextField(verbose_name = 'укажите описание книги', null=True , blank=True)
    price = models.FloatField(verbose_name = 'укажите ценник книги', null=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name = 'укажите дата создания книги', null=True)
    genre = models.CharField(max_length=10, choices=GENRE ,verbose_name = 'укажите жанр книги', null=True)
    email = models.EmailField(verbose_name = 'укажите email', null=True)
    director = models.CharField(max_length=100,verbose_name = 'укажите создателя книги', null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

class Reviews(models.Model):
    GRADE = (
        ('⭐','⭐'),
        ('⭐⭐️','⭐⭐️'),
        ('⭐⭐⭐️','⭐⭐⭐️'),
        ('⭐⭐⭐⭐️','⭐⭐⭐⭐️'),
        ('⭐⭐⭐⭐⭐️','⭐⭐⭐⭐⭐️'),
    )
    choice_book = models.ForeignKey(Books, on_delete=models.CASCADE,
                                    related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    grade = models.CharField(max_length=10, choices=GRADE, default='⭐️')
    def __str__(self):
        return f'{self.choice_book.title} - {self.grade}'