from django.db import models


# from django.contrib.auth import get_user_model
# #
# User = get_user_model()


class Author(models.Model):
    username: str = models.CharField(max_length=50, verbose_name='Имя пользователя')
    first_name: str = models.CharField(max_length=50, verbose_name='Имя', null=True)
    last_name: str = models.CharField(max_length=50, verbose_name='Фамилия', null=True, blank=True)
    email: str = models.EmailField(max_length=127, verbose_name='Email')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    avatar = models.ImageField(upload_to='author_avatars')
    password: str = models.CharField(max_length=127, verbose_name='Пароль')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Post(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts', null=True)
    title = models.CharField(max_length=127, verbose_name='Заголовок', null=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='post_images/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    raiting = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Коммент к посту: {self.post.title} от автора: {self.post.user} комментатор: {self.author.username}'

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комментарии'
