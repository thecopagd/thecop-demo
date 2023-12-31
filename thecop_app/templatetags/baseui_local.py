from django import template

register = template.Library()


@register.inclusion_tag('thecop_app/localAdmin/base.html')
def header_component():
    pass
