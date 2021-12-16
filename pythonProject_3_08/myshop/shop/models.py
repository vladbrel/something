from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True) #unique т.е. имя должно быть уникальным

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):  # магич метод, кот относ к модели продукта
        return self.name

    class Meta:
        ordering=('name',)
        verbose_name='Категория'
        verbose_name_plural='Категории'
class Product(models.Model):

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    name = models.CharField(max_length=200,                            db_index=True)  # db=True значит, что в бд там будет именно эти столбы искать и так быстрее
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)  # blank=true- мб не быть картинки, т.е. БД может хранить пустое знач.
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')  # Cascade: если удаляется категоиия, то удалятся все товары этой категории

    def __str__(self):  # магич метод, кот относ к модели продукта
        return self.name

    class Meta:  # спец мета класс, кот доб настройки к нашему классу, класс-обёртка, расширяет наш объект
        ordering = ('name',)  # sort by name
        index_together = (('id', 'slug'),)  # совместный поиск по id и slug раздельно
        verbose_name='Продукты'
        index_together=(('id', 'slug'),)

class TestUser(models.Model):
    login = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

# class Matras(models.Model):
#     name = models.CharField(max_length=150)
#     color = models.CharField(max_length=150)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     description = models.TextField()
#
# class Bed(models.Model):
#     name = models.CharField(max_length=150)
#     color = models.CharField(max_length=150)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     description = models.TextField(
#
# class Store(models.Model):
#     name = models.CharField(max_length=150)
#     color = models.CharField(max_length=150)
#     description = models.TextField()