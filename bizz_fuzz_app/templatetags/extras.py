from django import template
from datetime import date

register = template.Library()


@register.filter(name='count_eligible')
def count_eligible(birth_date):
    today = date.today()
    if today.month < birth_date.month or\
        (today.month == birth_date.month and today.day < birth_date.day):
        age = today.year - birth_date.year - 1
    else:
        age = today.year - birth_date.year
    if age > 13:
        return "Allowed"
    else:
        return "Blocked"


@register.filter(name='count_bizzfuzz')
def count_bizzfuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "BizzFuzz"
    elif number % 3 == 0:
        return "Bizz"
    elif number % 5 == 0:
        return "Fuzz"
    else:
        return number