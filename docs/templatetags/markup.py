from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def markup(value):
    from docs.templatetags.markdown import markdown
    return markdown(value)
