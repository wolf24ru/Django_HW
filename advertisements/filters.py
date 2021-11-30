import django_filters
from django_filters import DateFromToRangeFilter, widgets
from django_filters import FilterSet
from django_filters.widgets import RangeWidget

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    updated_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'updated_at']
