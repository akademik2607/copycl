from django.db import models

# Create your models here.
from apps.archives.models import ArchiveBase
from apps.user.models import CustomUser

NULLABLE = {
    'null': True,
    'blank': True
}


class SubscriptionPeriod(models.Model):
    name = models.CharField('Название свойства', max_length=125, null=False)
    days = models.IntegerField('Количество дней', **NULLABLE)
    price = models.IntegerField('Стоимость варианта подписки')
    percent_for_key = models.IntegerField('Какой процент стоимости для ключа', **NULLABLE)
    product = models.ForeignKey('Product', related_name='period', verbose_name='Продукт', on_delete=models.CASCADE)
    created_at = models.DateTimeField('Время создания', auto_now_add=True)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    class Meta:
        verbose_name = 'Срок подписки'
        verbose_name_plural = 'Сроки подписки'


class Product(models.Model):
    name = models.CharField('Название продукта', max_length=125, null=False)
    slug = models.SlugField('Слаг', max_length=200, **NULLABLE)
    image = models.ImageField('Изображение товара', max_length=300)
    description = models.TextField('Описание')
    download_link = models.URLField('Ссылка для скачивания')


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_subscription', on_delete=models.CASCADE)
    archive = models.ForeignKey(ArchiveBase, on_delete=models.CASCADE)
    begin_access = models.DateField('Начало действия подписки', **NULLABLE)
    expire_access = models.DateField('Окончание действия подписки', **NULLABLE)
    count_keys = models.IntegerField('Количество ключей', **NULLABLE)
    created_at = models.DateTimeField('Время создания', auto_now_add=True)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)



class Order(models.Model):
    pass
