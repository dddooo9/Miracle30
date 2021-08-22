from django import template
register = template.Library()

@register.filter
def index_1(indexable, i):
    return indexable[i]


@register.filter
def index_2(indexable, i):
    return indexable[i+10]


@register.filter
def index_3(indexable, i):
    return indexable[i+20]

