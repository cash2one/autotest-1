from django import template
register = template.Library()
@register.filter(name='key')
def key(d,key):
    value = []
    try:
        rk = "%s"%key
        value = d[rk]
    except KeyError:
        value = []
    return value

@register.filter(name='delete')
def delete(d,key):
    if(key==0 or key==2 or key==3 or key==5):
        return 1
    return 0

@register.filter(name='start')
def start(d,key):
    if(key==0 or key==5):
        return 1
    return 0

@register.filter(name='stop')
def stop(d,key):
    if(key==2):
        return 1
    return 0

@register.filter(name='get_id')
def get_id(value):
    return value["_id"]

@register.filter(name='result')
def result(d,key):
    return d[key]
