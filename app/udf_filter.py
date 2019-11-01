from django import template


register=template.Library()

def cut(value,args):
    return value.replace(args,"")

def reverse(value,args):
    return value[::-1]

register.filter('reverse',reverse)
register.filter('cut',cut)