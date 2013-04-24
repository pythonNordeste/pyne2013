from django import template


register = template.Library()


@register.filter
def format_phone(phone):
    if '-' not in phone:
        return u'{0} {1}-{2}'.format(phone[:2], phone[2:6], phone[6:])
    return phone
