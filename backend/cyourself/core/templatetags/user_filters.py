from django import template 


register = template.Library() 

@register.filter 
def addclass(field, css): 
    return field.as_widget(attrs={'class': css})

@register.filter(name='get_fields')
def get_fields(obj):
    if hasattr(obj, '__dict__'):
        return obj.__dict__.items()
    return []