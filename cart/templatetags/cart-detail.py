from django import template

register = template.Library()

from cart import cart

@register.simple_tag
def car_itens(self):
    return sum(item["quantity"] for item in self.cart.values())