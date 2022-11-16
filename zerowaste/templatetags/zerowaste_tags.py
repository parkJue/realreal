from django import template

register = template.Library()


@register.filter
def at(obj, key):
    return obj[key]