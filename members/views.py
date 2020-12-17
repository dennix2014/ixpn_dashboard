from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
import uuid
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from .models import PortConnection, Fee, POP, Organisation
from .filters import PortFilter
from .forms import OrganisationForm, POPForm, FeeForm, PortConnectionForm
# Create your views here.


def home(request):
    pp = PortConnection.objects.filter(member__status='active').order_by('member__name')
    ports = PortConnection.objects.all().order_by('member__name')
    charges = Fee.objects.all()
    pops = POP.objects.all()
    organisations = Organisation.objects.all().order_by('name')
    f = PortFilter(request.GET, queryset=ports)
    html = ''
    table_body = ''
    total_port_charges = 0
    total_membership_fee = 0
    port_count = 0
    table_heading = """
    <table><caption>ALL MEMBERS</caption>
        <tr>
            <th>S/NO</th>
            <th>Menber</th>
            <th>POP</th>
            <th>PORT CAPACITY</th>
            <th>MEMBERSHIP</th>
            <th>STATUS</th>
            <th>NO OF PORTS</th>
            <th>PORT FEE</th>
            <th>MEMBERSHIP FEE</th>
            
         
         
        </tr>"""
    for index, item in enumerate(f.qs):
        table_body += (f'<tr>'
        f'<td>{index + 1}</td>'
        f'<td><a href="/port_connection/{item.id}/{item.slug}/"><h6>{ item.member }</h6></a></td>'
        f'<td>{item.pop}</td>'
        f'<td>{item.port_capacity}</td>'
        f'<td>{item.member.membership}</td>'
        f'<td>{item.member.status}</td>'
        f'<td>{item.no_of_port}</td>')

        for charge in charges:
            if charge.port_capacity == item.port_capacity and \
                item.member.status == 'active' and \
                item.member.membership == 'full':
                port_charge = item.no_of_port * charge.port_fee
                membership_fee = charge.membership_fee
                total_port_charges += port_charge
                total_membership_fee += membership_fee
                table_body += f'<td>{(port_charge):,}</td>'
                table_body += f'<td>{(membership_fee):,}</td>'
            elif (item.member.status == 'inactive' or \
                item.member.membership == 'associate') and \
                charge.port_capacity == item.port_capacity:
                table_body += f'<td>0</td>'
                table_body += f'<td>0</td>'

        table_body +=  f'</tr>'
        port_count += item.no_of_port
    table_body += (f'<tr><td><strong>TOTALS</strong></td><td> - </td><td> - </td><td> - </td><td></td>'
                    f'<td></td><td>{port_count}</td><td>{(total_port_charges):,}</td>'
                    f'<td>{(total_membership_fee):,}</td></tr>')
      
    table_body += f'</table> <br><br><br>'

    html = table_heading + table_body

    context = {
        'html':html, 
        'filter': f, 
        'pops': pops,
        'organisations': organisations,
        'charges': charges,
        'pp': pp}
   

    return render(request, 'home.html', context)



def edit_pop(request, pk, slug):
    pops = POP.objects.get(pk=pk)
    if request.method == 'POST':
        form = POPForm(request.POST, request.FILES, instance=pops)
        if form.is_valid():
            pops.save()
            messages.success(request, 'POP edited successfully')
            return redirect('home')

    elif request.method == 'GET':
        form = POPForm(instance=pops)
        return render(request, 'edit_pop.html', {'form': form} )


def edit_organisation(request, pk, slug):
    organisations = Organisation.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrganisationForm(request.POST, request.FILES, instance=organisations)
        if form.is_valid():
            organisations.save()
            messages.success(request, 'organisation edited successfully')
            return redirect('home')

    elif request.method == 'GET':
        form = OrganisationForm(instance=organisations)
        return render(request, 'edit_organisation.html', {'form': form} )


def edit_port_connection(request, pk, slug):
    port_connections = PortConnection.objects.get(pk=pk)
    if request.method == 'POST':
        form = PortConnectionForm(request.POST, request.FILES, instance=port_connections)
        if form.is_valid():
            port_connections.save()
            messages.success(request, 'PortConnection edited successfully')
            return redirect('home')

    elif request.method == 'GET':
        form = PortConnectionForm(instance=port_connections)
        return render(request, 'edit_port_connection.html', {'form': form} )

def edit_port_charge(request, pk, slug):
    port_charges = Fee.objects.get(pk=pk)
    if request.method == 'POST':
        form = FeeForm(request.POST, request.FILES, instance=port_charges)
        if form.is_valid():
            port_charges.save()
            messages.success(request, 'Fees edited successfully')
            return redirect('home')

    elif request.method == 'GET':
        form = FeeForm(instance=port_charges)
        return render(request, 'edit_port_charge.html', {'form': form} )

def add_pop(request):
    pop_obj = POP()
    if request.method == 'POST':
        form = POPForm(request.POST, request.FILES)
        if form.is_valid():
            pop_obj.name =  request.POST['name']
            pop_obj.state_located =  request.POST['state_located']
            pop_obj.created_by = request.user
            pop_obj.save()
            return redirect('home')

    elif request.method == 'GET':
        form = POPForm()
        return render(request, 'edit_pop.html', {'form': form})


def add_port_charge(request):
    port_charge_obj = Fee()
    if request.method == 'POST':
        form = FeeForm(request.POST, request.FILES)
        if form.is_valid():
            port_charge_obj.port_capacity = request.POST['port_capacity']
            port_charge_obj.port_fee =  request.POST['port_fee']
            port_charge_obj.membership_fee =  request.POST['membership_fee']
            port_charge_obj.created_by = request.user
            port_charge_obj.save()
            return redirect('home')

    elif request.method == 'GET':
        form = FeeForm()
        return render(request, 'edit_port_charge.html', {'form': form})

def add_organisation(request):
    organisation_obj = Organisation()
    if request.method == 'POST':
        form = OrganisationForm(request.POST, request.FILES)
        if form.is_valid():
            organisation_obj.name =  request.POST['name']
            organisation_obj.status = request.POST['status']
            organisation_obj.membership = request.POST['membership']
            organisation_obj.date_joined = request.POST['date_joined']
            organisation_obj.created_by = request.user
            organisation_obj.save()
            return redirect('home')

    elif request.method == 'GET':
        form = OrganisationForm()
        return render(request, 'edit_organisation.html', {'form': form})

def add_port_connection(request):
    port_connection_obj = PortConnection()
    if request.method == 'POST':
        form = PortConnectionForm(request.POST, request.FILES)
        if form.is_valid():
            port_connection_obj.member_id = request.POST['member']
            port_connection_obj.pop_id = request.POST['pop']
            port_connection_obj.no_of_port = request.POST['no_of_port']
            port_connection_obj.port_capacity = request.POST['port_capacity']
            port_connection_obj.created_by = request.user
            
            port_connection_obj.save()
            return redirect('home')

    elif request.method == 'GET':
        form = PortConnectionForm()
        return render(request, 'edit_port_connection.html', {'form': form})
''