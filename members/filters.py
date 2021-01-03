import django_filters
from .models import PortConnection
from .all_choices import status, membership

class PortFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(field_name='member_name', 
        method='filter_status', label='Status', choices=status)

    membership = django_filters.ChoiceFilter(field_name='member_name', 
        method='filter_membership', label='Membership', choices=membership)

    date_connected_min = django_filters.DateFilter(field_name='date_connected', 
        lookup_expr='gte', label='Date start')

    date_connected_max = django_filters.DateFilter(field_name='date_connected', 
        lookup_expr='lte', label='Date end')
         
    def filter_status(self, queryset, name, value):
        return queryset.filter(member_name__status=value)

    def filter_membership(self, queryset, name, value):
        return queryset.filter(member_name__membership=value)

    def filter_pop(self, queryset, name, value):
        return queryset.filter(switch__pop=value)


    class Meta:
        model = PortConnection
        fields = {
            'port_capacity': ['exact',],
            'switch': ['exact'],
            'member_name': ['exact']
        
        }
      

   