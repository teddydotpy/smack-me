from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def year():
    return datetime.now().year