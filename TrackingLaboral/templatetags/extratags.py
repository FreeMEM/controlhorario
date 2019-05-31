from django import template
from datetime import datetime

register = template.Library()

@register.filter
def dateStrToDayWeek(value):
    try:
        return datetime.strptime(value,"%Y-%m-%d").strftime('%A')
    except:
        return ""


register.filter('dateStrToDayWeek',dateStrToDayWeek)