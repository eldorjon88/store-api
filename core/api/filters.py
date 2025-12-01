from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    stock = filters.NumberFilter(field_name="stock")
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'stock', 'created_at']
