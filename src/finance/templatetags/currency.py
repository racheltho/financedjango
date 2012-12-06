from django.contrib.humanize.templatetags.humanize import intcomma
from django import template

#from django.conf import settings
#import re
#from django.utils.encoding import force_unicode
#from django.utils.formats import number_format
#def intcomma(value, use_l10n=True):
#    """
#    Converts an integer to a string containing commas every three digits.
#    For example, 3000 becomes '3,000' and 45000 becomes '45,000'.
#    """
#    if settings.USE_L10N and use_l10n:
#        try:
#            if not isinstance(value, float):
#                value = int(value)
#        except (TypeError, ValueError):
#            return intcomma(value, False)
#        else:
#            return number_format(value, force_grouping=True)
#    orig = force_unicode(value)
#    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', orig)
#    if orig == new:
#        return new
#    else:
#        return intcomma(new, use_l10n)



def currency(dollars):
    dollars = round(float(dollars), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])

register = template.Library()
register.filter('currency', currency)