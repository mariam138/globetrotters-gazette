# Code to create custom filter is adapted from the Django docs
# https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/#how-to-create-custom-template-tags-and-filters

from django import template
from ..models import REGIONS

register = template.Library()

@register.filter
def get_region_name(region_code, is_safe=True):
    # Create a dictionary from the REGIONS choices list in models.py
    regions_dict = dict(REGIONS)
    # Will return the region name of the region_code that is specified
    return regions_dict.get(region_code)
