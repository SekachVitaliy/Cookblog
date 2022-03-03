from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100, verbose_name='категория')
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.lower()
        return super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='тег')
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.lower()
        return super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.lower()
        return super(Post, self).save(*args, **kwargs)

    def get_recipes(self):
        return self.recipes.all()


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(
        Post,
        related_name="recipes",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Рецепт'
        verbose_name = 'Рецепты'


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
