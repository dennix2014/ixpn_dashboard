import django_filters
from .models import PortConnection
from .all_choices import status, membership

class PortFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(field_name='member_name', 
        method='filter_status', label='Status', choices=status)

    membership = django_filters.ChoiceFilter(field_name='member_name', 
        method='filter_membership', label='Membership', choices=membership)

    date_connected_min = django_filters.DateFilter(field_name='date_connected', 
        lookup_expr='gte', label='Date Connected   start')

    date_connected_max = django_filters.DateFilter(field_name='date_connected', 
        lookup_expr='lte', label='Date Connected end')

    no_of_port = django_filters.ChoiceFilter(field_name='no_of_port', 
        lookup_expr='gte', label='No of Ports (GTE)', 
        choices=list(zip(range(1, 16), range(1, 16))))
            

    def filter_status(self, queryset, name, value):
        return queryset.filter(member_name__status=value)

    def filter_membership(self, queryset, name, value):
        return queryset.filter(member_name__membership=value)

    class Meta:
        model = PortConnection
        fields = {
            'pop': ['exact',],
            'port_capacity': ['exact',]
        }
      

   