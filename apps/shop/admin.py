from django.contrib import admin
from django.contrib.admin import TabularInline

from apps.shop.models import Product, SubscriptionPeriod, Subscription


class SubscriptionPeriodInline(TabularInline):
    model = SubscriptionPeriod
    extra = 0




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [SubscriptionPeriodInline]



@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass