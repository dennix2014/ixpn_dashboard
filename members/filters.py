import django_filters
from .models import PortConnection
from .all_choices import status, membership

class PortFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(field_name='member_name', 
        method='filter_status', label='Status', choices=status)

    membership = django_filters.ChoiceFilter(field_name='member_name', 
        method='filter_membership', label='Membership', choices=membership)

    date_joined_min = django_filters.DateFilter(field_name='member_name.date_joined', 
        method='filter_date_joined_min', label='Date Joined start')

    date_joined_max = django_filters.DateFilter(field_name='member_name.date_joined', 
        method='filter_date_joined_max', label='Date Joined end')

    no_of_port = django_filters.ChoiceFilter(field_name='no_of_port', 
        lookup_expr='gte', label='No of Ports (GTE)', 
        choices=list(zip(range(1, 16), range(1, 16))))
            

    def filter_status(self, queryset, name, value):
        return queryset.filter(member_name__status=value)

    def filter_membership(self, queryset, name, value):
        return queryset.filter(member_name__membership=value)

    def filter_date_joined_min(self, queryset, name, value):
        return queryset.filter(member_name__date_joined__gte=value)

    def filter_date_joined_max(self, queryset, name, value):
        return queryset.filter(member_name__date_joined__lte=value)

    class Meta:
        model = PortConnection
        fields = {
            'pop': ['exact',],
            'port_capacity': ['exact',]
        }
      

   