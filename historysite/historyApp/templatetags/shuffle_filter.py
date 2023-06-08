from django import template
import random

register = template.Library()


@register.filter
def shuffle(arg):
    temp = list(arg)
    random.shuffle(temp)
    return temp
