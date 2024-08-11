from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Заголовок поста
    content = models.TextField()  # Содержание поста
    published_date = models.DateTimeField(auto_now_add=True)  # Дата публикации

    def __str__(self):
        return self.title
