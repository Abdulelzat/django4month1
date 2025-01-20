from django.db import models

class Book(models.Model):
    GENRE_CHOICES = (
        ('Ужасы', 'Ужасы'),
        ('Комедия','Комедия'),
        ('Романтика', 'Романтика')
    )
    image = models.ImageField(upload_to='books/', verbose_name='Изображение', null=True, blank=True)
    title = models.CharField(max_length=100,verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name= 'Цена')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата cоздание')
    genre = models.CharField(choices=GENRE_CHOICES, max_length=100,verbose_name='Жанр')
    email = models.EmailField(verbose_name='Почта')
    author = models.CharField(max_length=50,verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

