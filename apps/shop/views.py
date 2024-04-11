from django.shortcuts import render
from django.views.generic import DetailView

from apps.shop.models import Subscription, Product


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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/detail_product.html'


def ordering(request):

    return render(request, 'shop/ordering.html', context={

    })
