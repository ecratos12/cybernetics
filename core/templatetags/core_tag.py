# -*- coding: utf-8 -*-

from django import template
register = template.Library()
from core.models import *

@register.inclusion_tag('tags/department.html')
def department():
	items = Department.objects.all()
	return {'items':items }