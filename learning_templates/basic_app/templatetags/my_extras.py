from django import template

register = template.Library()

@register.filter(name='chop')
def cutme(value,arg):
    return value.replace(arg,'')

# register.filter('chop',cutme)
