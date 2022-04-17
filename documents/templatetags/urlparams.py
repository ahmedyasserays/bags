from urllib import request
from wsgiref.util import request_uri
from django import template
from urllib.parse import urlencode


register = template.Library()
@register.simple_tag(takes_context=True)
def urlparams(context,*_, **kwargs):
    request = context['request']
    if request:
        return '?{}'.format(urlencode(request.GET))
    return ''

@register.simple_tag(takes_context=True)
def values(context,*_, **kwargs):
    request = context['request']
    if request:
        return request.GET
    return ''
