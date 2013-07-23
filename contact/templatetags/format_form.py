# -*- coding:utf:8 -*-
from django import template
from django.template.loader import get_template


register = template.Library()


@register.filter
def format_form(form):
    t = get_template("templatetags/form.html")
    return t.render(template.Context({'form': form}))
