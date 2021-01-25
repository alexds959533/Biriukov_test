from django_filters import rest_framework as filters
from .models import Shop


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ShopFilter(filters.FilterSet):
    city = CharFilterInFilter(field_name='city__name', lookup_expr='in')
    street = CharFilterInFilter(field_name='street__name', lookup_expr='in')

    class Meta:
        model = Shop
        fields = ['city', 'street']