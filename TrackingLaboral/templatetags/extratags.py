from django import template
from datetime import datetime

register = template.Library()

@register.filter
def dateStrToDayWeek(value):
    return datetime.strptime(value,"%Y-%m-%d").strftime('%A')


register.filter('dateStrToDayWeek',dateStrToDayWeek)