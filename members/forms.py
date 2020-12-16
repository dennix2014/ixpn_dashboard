from django.forms import ModelForm
from .models import POP, Fee, PortConnection, Organisation

class POPForm(ModelForm):
    class Meta:
        model = POP
        fields = ['name', 'state_located']

class FeeForm(ModelForm):
    class Meta:
        model = Fee
        fields = ['port_capacity', 'port_fee', 'membership_fee']

class PortConnectionForm(ModelForm):
    class Meta:
        model = PortConnection
        fields = ['member', 'pop', 'port_capacity', 'no_of_port']

class OrganisationForm(ModelForm):
    class Meta:
        model = Organisation
        fields = ['name', 'status', 'membership_type', 'date_joined']