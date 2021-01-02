from django import forms
from .models import POP, PortConnection, Member, Switch, SwitchPort, Aka

class POPForm(forms.ModelForm):
    class Meta:
        model = POP
        fields = ['name', 'state_located']

class PortConnectionForm(forms.ModelForm):
    class Meta:
        model = PortConnection
        fields = ['member_name', 'pop', 'port_capacity', 
        'no_of_port', 'port_fee', 'membership_fee', 'date_connected']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['short_name', 'status', 'membership']


class SwitchPortForm(forms.ModelForm):
    class Meta:
        model = SwitchPort
        fields = ['name', 'switch', 'int_type']

class SwitchForm(forms.ModelForm):
    class Meta:
        model = Switch
        fields = ['manufacturer', 'model', 'serial_no']

class AkaForm(forms.ModelForm):
    class Meta:
        model = Aka
        fields = ['memname', 'switch', 'pot']