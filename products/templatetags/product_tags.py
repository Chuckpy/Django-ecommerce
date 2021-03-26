from django import template

register =template.Library()

@register.filter()
def remainder(n):
    return n % 3