from django import forms
from django.conf import settings

PRODUCT_QUANTITY_CHOICES = [
    (i, str(i)) for i in range(1, settings.CART_ITEM_MAX_QUANTITY + 1)
]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        label="Quantidade", choices=PRODUCT_QUANTITY_CHOICES, coerce=int
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )