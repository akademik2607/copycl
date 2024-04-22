from django import forms

from apps.shop.models import OrderItem


class SingleProductForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['subscription_period', 'count_keys']




