from django import template

register=template.Library()

@register.filter
def redondear(valor,decimal=2):
    va=float(valor)
    return round(va,decimal)