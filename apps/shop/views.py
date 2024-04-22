import datetime

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.archive import Archive
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from apps.archives.models import ArchiveBase, Key
from apps.shop.forms import SingleProductForm
from apps.shop.models import Subscription, Product, SubscriptionPeriod, Order, ORDER_STATUSES, OrderItem


def shop(request):
    user = request.user
    if user.is_authenticated:
        subscriptions = Subscription.objects.filter(user=user)
        products = Product.objects.all()
        return render(
            request,
            'shop/index.html',
            context={
                'products': products,
                'subscription': subscriptions
            })
    else:
        return render(
            request,
            'shop/index.html'
        )


class ProductDetailView(DetailView, FormMixin):
    model = Product
    form_class = SingleProductForm
    template_name = 'shop/detail_product.html'


def ordering(request):
    for item in request.POST:
        print(item)

    count_keys = request.POST.get('count_keys')
    product_id = request.POST.get('product_id')
    subscription_period_id = request.POST.get('subscription_period')
    user = request.user

    product = get_object_or_404(Product, pk=product_id)

    subscription_period = get_object_or_404(SubscriptionPeriod, pk=subscription_period_id)
    subscription_period_price = subscription_period.price
    key_percent_price = subscription_period.percent_for_key

    key_price = subscription_period_price // 100 * key_percent_price
    config_price = subscription_period_price - key_price
    summary_keys_price = key_price * int(count_keys)
    total_price = summary_keys_price + config_price

    return render(request, 'shop/ordering.html', context={
        'product_id': product_id,
        'product_name': product.name,
        'subscription_period_name': subscription_period.name,
        'subscription_period_price': subscription_period_price,
        'subscription_period_id': subscription_period.id,
        'count_keys': count_keys,
        'key_price': key_price,
        'summary_keys_price': summary_keys_price,
        'config_price': config_price,
        'total_price': total_price
    })


def create_order_view(request):
    for item in request.POST:
        print(item)

    product_id = request.POST.get('product_id')
    subscription_id = request.POST.get('subscription_id', None)
    subscription_period_id = request.POST.get('subscription_period_id')
    email = request.POST.get('email', None)
    phone = request.POST.get('phone', None)
    try:
        count_keys = int(request.POST.get('count_keys'))
    except Exception:
        # return reverse("shop:ordering")
        pass
    # if not count_keys or count_keys <= 0:
    #     return reverse("shop:ordering")


    product = get_object_or_404(Product, pk=product_id)
    subscription_period = get_object_or_404(SubscriptionPeriod, pk=subscription_period_id)
    OrderItem(
        product=product,
        subscription_period=subscription_period,
        count_keys=count_keys
    ).save()
    order_item = OrderItem.objects.last()
    subscription = None
    if subscription_id:
        pass #TODO

    print(type(order_item))
    # Order(
    #     order_product=order_item,
    #     subscription=subscription,
    #     status=ORDER_STATUSES[0][0],
    #     user=request.user,
    #     email=email,
    #     order_user_phone=phone
    # ).save()
    # order = Order.objects.last()

    #start test!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    ArchiveBase(
        name=request.user.email,
        user=request.user
    ).save()
    archive = ArchiveBase.objects.last()

    Key.objects.bulk_create([Key(archive_base=archive) for i in range(count_keys)])
        # archive_base = models.ForeignKey(ArchiveBase, on_delete=models.CASCADE)
        # access_key = models.CharField('Ключ доступа', max_length=250)
        # hwid = models.CharField('HWID', max_length=25, **NULLABLE)
        # is_active = models.BooleanField('Активен', default=True)
        # created_at = models.DateTimeField('Время создания', auto_now_add=True)
        # updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    Subscription(
        user=request.user,
        product=product,
        archive=archive,
        begin_access=datetime.date.today(),
        expire_access=datetime.date.today() + datetime.timedelta(days=subscription_period.days),
        count_keys=count_keys,
        is_active=True,
    ).save()
    subscription = Subscription.objects.last()
    Order(
        order_product=order_item,
        subscription=subscription,
        status=ORDER_STATUSES[2][0],
        user=request.user,
        email=email,
        order_user_phone=phone
    ).save()
    order = Order.objects.last()
    return render(request, 'shop/pay_confirm.html', context={})
    #end test!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # return render(request, 'shop/pay_confirm.html', context={
    #     'order_number': order.order_number
    # })


# class Order(models.Model):
#     order_product = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
#     subscription_id = models.IntegerField('Id подписки', **NULLABLE)
#     status = models.CharField('Статус заказа', max_length=20, choices=ORDER_STATUSES, default=ORDER_STATUSES[0][0])
#     created_at = models.DateTimeField('Время создания', auto_now_add=True)
#     updated_at = models.DateTimeField('Последнее обновление', auto_now=True)
#     user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
#     email = models.EmailField('Email', **NULLABLE)
#     order_user_phone = models.CharField('Телефон', max_length=25, **NULLABLE)