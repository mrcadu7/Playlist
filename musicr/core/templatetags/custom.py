from django import template

register = template.Library()


@register.filter
def ms_to_minutes_and_seconds(ms):
    total_seconds = ms / 1000
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    return f"{minutes}:{seconds:02d}"