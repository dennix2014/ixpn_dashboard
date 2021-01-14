from django import forms
from .models import POP, PortConnection, Member, Switch, SwitchPort

class POPForm(forms.ModelForm):
    class Meta:
        model = POP
        fields = ['name', 'state_located']

class PortConnectionForm(forms.ModelForm):
    
   
    class Meta:
        model = PortConnection
        fields = ['member_name', 'port_capacity', 'switch', 'switch_port',
        'port_fee', 'membership_fee', 'date_connected']

        labels = {
            'membership_fee': 'Annual Membership Fee',
            'port_fee': 'Monthly Port Fee'
        }


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['short_name', 'status', 'membership']


class SwitchPortForm(forms.ModelForm):
    class Meta:
        model = SwitchPort
        fields = ['name', 'switch', 'int_type', 'media']

class SwitchForm(forms.ModelForm):
    class Meta:
        model = Switch
        fields = ['name', 'oem', 'model', 'serial_no', 'pop', 'ipv4_address']

