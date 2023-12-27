from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.inclusion_tag('thecop_app/header_component.html')
def header_component(active):
    return {
        "active": active,
    }