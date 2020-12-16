import django_filters
from .models import PortConnection

class PortFilter(django_filters.FilterSet):
    # is_active = django_filters.BooleanFilter(field_name='member', method='filter_is_active', label='Member active')

    # def filter_is_active(self, queryset, name, value):
    #     return queryset.filter(member__is_active=value)

    class Meta:
        model = PortConnection
        fields = {
            'no_of_port': ['exact'],
            'pop': ['exact',],
            'port_capacity': ['exact',],
        }
      

   