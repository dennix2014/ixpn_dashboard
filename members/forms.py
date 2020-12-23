from django.forms import ModelForm
from .models import POP, PortConnection, Member

class POPForm(ModelForm):
    class Meta:
        model = POP
        fields = ['name', 'state_located']

class PortConnectionForm(ModelForm):
    class Meta:
        model = PortConnection
        fields = ['member_name', 'pop', 'port_capacity', 
        'no_of_port', 'port_fee', 'membership_fee', 'date_connected']

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['short_name', 'status', 'membership']