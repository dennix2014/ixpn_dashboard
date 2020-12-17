import django_filters
from .models import PortConnection
from .all_choices import status, membership

class PortFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(field_name='member', \
        method='filter_status', label='Status', choices=status)

    membership = django_filters.ChoiceFilter(field_name='member', \
        method='filter_membership', label='Membership', choices=membership)

    date_joined_min = django_filters.DateFilter(field_name='member.date_joined', \
        method='filter_date_joined_min', label='Date Joined after')

    date_joined_max = django_filters.DateFilter(field_name='member.date_joined', \
        method='filter_date_joined_max', label='Date Joined before')

    no_of_port = django_filters.NumberFilter(field_name='no_of_port', \
        lookup_expr='gte', label='No of Ports (GTE)')
            

    def filter_status(self, queryset, name, value):
        return queryset.filter(member__status=value)

    def filter_membership(self, queryset, name, value):
        return queryset.filter(member__membership=value)

    def filter_date_joined_min(self, queryset, name, value):
        return queryset.filter(member__date_joined__gte=value)

    def filter_date_joined_max(self, queryset, name, value):
        return queryset.filter(member__date_joined__lte=value)

    class Meta:
        model = PortConnection
        fields = {
            'pop': ['exact',],
            'port_capacity': ['exact',],
        }
      

   