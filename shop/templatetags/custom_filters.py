from django import template

register = template.Library()


@register.filter
def multiply(v1, v2):
    return v1 * v2


@register.filter
def multiply_plus_add(v1, add_value):
    return multiply(v1, add_value) + add_value

@register.filter
def get_type(val):
    print(type(val))
    return type(val)
