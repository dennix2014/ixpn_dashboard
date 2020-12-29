from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
import uuid
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from .models import PortConnection, POP, Member
from .filters import PortFilter
from .forms import MemberForm, POPForm, PortConnectionForm
permission_denied_msg = """
Permission denied. Please contact app admin if you feel this is a mistake"""

@login_required
def home(request):

    ports = PortConnection.objects.all().order_by('member_name__short_name')
    f = PortFilter(request.GET, queryset=ports)
    total_port_fees_anum = 0
  
    total_membership_fee_anum = 0

    port_count = 0
    
    table_body = """
    <div class="table-responsive">
    <table class=""><caption>ALL PORT CONNECTIONS</caption>
        <tr class="">
            <th class="index">S/No</th>
            <th class="member">Member</th>
            <th class="pop">POP</th>
            <th class="portc">Port Capacity</th>
            <th class="membership">Membership</th>
            <th class="status">Status</th>
            <th class="no_of_ports">No Of Ports</th>
            <th class="fees_anum">PortFee /Annum (&#x20A6;)</th>
            <th class="fees_qtr">PortFee /Quater (&#x20A6;)</th>
            <th class="fees_mon">PortFee /Month (&#x20A6;)</th>
            <th class="fees_anum">MembershipFee /Annum (&#x20A6;)</th>
            <th class="fees_qtr">MembershipFee /Quater (&#x20A6;)</th>
            <th class="fees_mon">MembershipFee /Month (&#x20A6;)</th>
            <th class="date">Date Connected</th>
            
        </tr>"""

    for index, port in enumerate(f.qs):
        table_body += f'<tr class=""><td class="index">{index + 1}</td>'

        #if request.user has the right permissions, then show edit option
        if request.user.has_perm('members.add_portconnection'):
            memb = f'<td class="member"><a href="/edit_portconnection/{port.id}/{port.slug}/">{port.member_name}</a></td>'
        else:
            memb =  f'<td class="member">{port.member_name}</td>'

        table_body += (f'{memb}'
        f'<td class="pop">{port.pop}</td>'
        f'<td class="portc">{port.port_capacity}</td>'
        f'<td class="membership">{port.member_name.membership}</td>'
        f'<td class="status">{port.member_name.status}</td>'
        f'<td class="no_of_ports">{port.no_of_port}</td>')
        
        """if member is active and a full member, then apply fees. Also count
            total no of ports"""
            
        if port.member_name.status == 'Active' and \
            port.member_name.membership == 'Full':
            table_body += f'<td class="fees_anum">{(port.port_fee):,}</td>'
            table_body += f'<td class="fees_qtr">{round(port.port_fee / 4):,}</td>'
            table_body += f'<td class="fees_mon">{round(port.port_fee / 12):,}</td>'
            table_body += f'<td class="fees_anum">{(port.membership_fee):,}</td>'
            table_body += f'<td class="fees_qtr">{round(port.membership_fee/4):,}</td>'
            table_body += f'<td class="fees_mon">{round(port.membership_fee/12):,}</td>'

            total_membership_fee_anum += round(port.membership_fee)
            total_port_fees_anum += round(port.port_fee)
                
        elif port.member_name.status == 'Inactive' or \
            port.member_name.membership == 'Associate':
            table_body += (f'<td class="fees_anum">0</td><td class="fees_qtr">0</td>'
                            f'<td class="fees_mon">0</td><td class="fees_anum">0</td>'
                            f'<td class="fees_qtr">0</td><td class="fees_mon">0</td>')

        port_count += port.no_of_port

        table_body += f'<td class="date">{port.date_connected}</td></tr>'

        # Add row for total no of port, total port and membership fee
    table_body += (f'<tr class=""><td class="index"><strong>TOTAL</strong></td>'
                    f'<td class="member"> - </td>'
                    f'<td class="pop"> - </td>'
                    f'<td class="portc"> - </td>'
                    f'<td class="membership"> - </td>'
                    f'<td class="status"> - </td>'
                    f'<td class="no_of_ports">{port_count}</td>'
                    f'<td class="fees_anum">{(total_port_fees_anum):,}</td>'
                    f'<td class="fees_qtr">{round((total_port_fees_anum/4)):,}</td>'
                    f'<td class="fees_mon">{round((total_port_fees_anum/12)):,}</td>'
                    f'<td class="fees_anum">{(total_membership_fee_anum):,}</td>'
                    f'<td class="fees_qtr">{round((total_membership_fee_anum)/4):,}</td>'
                    f'<td class="fees_mon">{round((total_membership_fee_anum)/12):,}</td>'
                    f'<td class="date"> - </td></tr>')
      
    table_body += f'</table></div><br>'
    context = {
        'html':table_body,
        'filter':f,}

    return render(request, 'home.html', context)

    
@login_required
def delete_member(request, pk, slug):
    p = Member.objects.get(pk=pk)
    p.delete()
    messages.success(request, f'{p} successfully deleted')
    return redirect('home')

@login_required
def add_or_edit_pop(request, pk=None, slug=None):
    if request.user.has_perm('members.add_pop'):
        pop_obj = get_object_or_404(POP, pk=pk) if pk else None
        form = POPForm(request.POST, request.FILES, instance=pop_obj)
        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                obj.created_by = request.user
                obj.save()
                messages.success(request, f'{obj} saved successfully')
                return redirect('home')
            else:
                form = POPForm(instance=pop_obj)
                messages.error(request, 'Correct errors indicated and try again')
                return render(request, 'add_or_edit_pop.html', {'form': form})

        elif request.method == 'GET':
            form = POPForm(instance=pop_obj)
            context = {'form': form, 'pop_obj': pop_obj}
            return render(request, 'add_or_edit_pop.html', context)

    else:
        messages.error(request, permission_denied_msg)
        return redirect('home')

@login_required
def add_or_edit_portconnection(request, pk=None, slug=None):
    if request.user.has_perm('members.add_portconnection'):
        portconnection_obj = get_object_or_404(PortConnection, 
                                        pk=pk) if pk else None

        form = PortConnectionForm(request.POST, request.FILES, 
                                instance=portconnection_obj)

        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                obj.created_by = request.user
                obj.save()
                messages.success(request, f'{obj} saved successfully')
                return redirect('home')
            else:
                form = PortConnectionForm(instance=portconnection_obj)
                messages.error(request, 'Correct errors indicated and try again')
                return render(request, 'add_or_edit_portconnection.html', 
                                                            {'form': form})

        elif request.method == 'GET':
            form = PortConnectionForm(instance=portconnection_obj)
            context = {'form': form, 'port_obj': portconnection_obj}
            return render(request, 'add_or_edit_portconnection.html', context)

    else:
        messages.error(request, permission_denied_msg)
        return redirect('home')


@login_required
def add_or_edit_member(request, pk=None, slug=None):
    if request.user.has_perm('members.add_member'):
        member_obj = get_object_or_404(Member, pk=pk) if pk else None
        form = MemberForm(request.POST, request.FILES, 
                                instance=member_obj)

        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                obj.created_by = request.user
                messages.success(request, f'{obj} saved successfully')
                obj.save()
                return redirect('home')
            else:
                form = MemberForm(instance=member_obj)
                messages.error(request, 'Correct errors indicated and try again')
                return render(request, 'add_or_edit_member.html', {'form': form})

        elif request.method == 'GET':
            form = MemberForm(instance=member_obj)
            context = {
                'form': form,
                'member_obj': member_obj,
            }
            return render(request, 'add_or_edit_member.html', context)

    else:
        messages.error(request, permission_denied_msg)
        return redirect('home')

@login_required
def list_members(request):
    members = Member.objects.all().order_by('short_name')

    table_body = """
    <table><caption>ALL MEMBERS</caption>
        <tr>
            <th>S/NO</th>
            <th>NAME</th>
            <th>STATUS</th>
            <th>MEMBERSHIP</th>
          
        </tr>"""

    for index, mem in enumerate(members):
        table_body += f'<tr><td>{index + 1}</td>'

        #if request.user has the right permissions, then show edit option
        if request.user.has_perm('members.add_member'):
            name = f'<td><a href="/edit_member/{mem.id}/{mem.slug}/">{mem.short_name}</a></td>'
        else:
            name =  f'<td>{mem.short_name}</td>'

        table_body += (f'{name}'
        f'<td>{mem.status}</td>'
        f'<td>{mem.membership}</td>')
    
    table_body += '</table>'

    context = {
        'html': table_body
    }
    return render(request, 'list_members.html', context)

@login_required
def list_pops(request):
    pops = POP.objects.all().order_by('name')

    table_body = """
    <table><caption>ALL POPS</caption>
        <tr>
            <th>S/NO</th>
            <th>NAME</th>
            <th>STATE LOCATED</th>
            <th>NO OF MEMBERS PRESENT</th>
        </tr>"""

    for index, pop in enumerate(pops):
        table_body += f'<tr><td>{index + 1}</td>'

        #if request.user has the right permissions, then show edit option
        if request.user.has_perm('members.add_pop'):
            name = f'<td><a href="/edit_pop/{pop.id}/{pop.slug}/">{pop.name}</a></td>'
        else:
            name =  f'<td>{pop.name}</td>'

        table_body += (f'{name}'
        f'<td>{pop.state_located}</td>'
        f'<td>{PortConnection.objects.all().filter(pop=pop.id).count()}</td></tr>')
    
    table_body += '</table>'
    
    context = {
        'html': table_body
    }
    return render(request, 'list_pops.html', context)

