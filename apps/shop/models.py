import uuid

from django.db import models

# Create your models here.
from apps.archives.models import ArchiveBase
from config.settings import AUTH_USER_MODEL

NULLABLE = {
    'null': True,
    'blank': True
}

ORDER_STATUSES = (
    ('rendering_payment', 'Ожидается оплата'),          #Заказ получен, оплата не совершена (заказ не оплачен).
    ('failed', 'Не удался'),                            #Платеж не прошел или был отклонен, или требует аутентификация (SCA).
    ('completed', 'Выполнен'),                          #Заказ выполнен и завершен, дальнейших действий не требуется.
    ('canceld', 'Отменен')                               #Заказ отменен администратором / менеджером магазина или покупателем.
)



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
        ordering = ['price']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название продукта', max_length=125, null=False)
    slug = models.SlugField('Слаг', max_length=200, **NULLABLE)
    image = models.ImageField('Изображение товара', max_length=300)
    description = models.TextField('Описание')
    download_link = models.URLField('Ссылка для скачивания')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_subscription', on_delete=models.CASCADE)
    archive = models.ForeignKey(ArchiveBase, on_delete=models.CASCADE)
    begin_access = models.DateField('Начало действия подписки', **NULLABLE)
    expire_access = models.DateField('Окончание действия подписки', **NULLABLE)
    count_keys = models.IntegerField('Количество ключей', **NULLABLE)
    is_active = models.BooleanField('Активна', default=False)
    created_at = models.DateTimeField('Время создания', auto_now_add=True)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subscription_period = models.ForeignKey(SubscriptionPeriod, verbose_name='Срок подписки', on_delete=models.CASCADE)
    count_keys = models.IntegerField('Количество ключей')


class Order(models.Model):
    order_product = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, **NULLABLE)
    status = models.CharField('Статус заказа', max_length=20, choices=ORDER_STATUSES, default=ORDER_STATUSES[0][0])
    created_at = models.DateTimeField('Время создания', auto_now_add=True)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField('Email', **NULLABLE)
    order_user_phone = models.CharField('Телефон', max_length=25, **NULLABLE)
     # = models.UUIDField('Номер заказа', )
    order_number = models.UUIDField('Номер заказа', default=uuid.uuid4, editable=False, unique=True)

