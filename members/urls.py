from django.urls import path

from . import views

urlpatterns = [

    path('edit_pop/<int:pk>/<slug:slug>/', 
        views.add_or_edit_pop, name='edit_pop'),

    path('add_pop/', 
        views.add_or_edit_pop, name='add_pop'),

    path('edit_member/<int:pk>/<slug:slug>/', 
        views.add_or_edit_member, name='edit_member'),

    path('add_member/', 
        views.add_or_edit_member, name='add_member'),

    path('edit_portconnection/<int:pk>/<slug:slug>/', 
        views.add_or_edit_portconnection, name='edit_portconnection'),

    path('add_portconnection/', 
        views.add_or_edit_portconnection, name='add_portconnection'),
    
	path('', 
        views.home, name='home'),

    path('delete_item/<int:pk>/<slug:slug>/<str:model>/', 
        views.delete_item, name='delete_item'),

    path('list_members/', 
        views.list_members, name='list_members'),

    path('list_pops/', 
        views.list_pops, name='list_pops'),

    path('edit_switch/<int:pk>/<slug:slug>/', 
        views.add_or_edit_switch, name='edit_switch'),

    path('add_switch/', 
        views.add_or_edit_switch, name='add_switch'),

    path('list_switches/', 
        views.list_switches, name='list_switches'),

    path('list_switch_ports/<int:pk>/<slug:slug>/', 
        views.list_switch_ports, name='list_switch_ports'),

    path('edit_switchport/<int:pk>/<slug:slug>/', 
        views.add_or_edit_switchport, name='edit_switchport'),

    path('add_switchport/', 
        views.add_or_edit_switchport, name='add_switchport'),

    path('ajax/load-ports/', views.ajax_load_ports, name='ajax_load_ports')

    
]