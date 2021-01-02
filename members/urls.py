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

    path('delete_organisation/<int:pk>/<slug:slug>/', 
        views.delete_member, name='delete_organisation'),

    path('list_members/', 
        views.list_members, name='list_members'),

    path('list_pops/', 
        views.list_pops, name='list_pops'),


    path('edit_switch/<int:pk>/<slug:slug>/', 
        views.add_or_edit_switch, name='edit_switch'),

    path('add_switch/', 
        views.add_or_edit_switch, name='add_switch'),

    path('edit_switchport/<int:pk>/<slug:slug>/', 
        views.add_or_edit_switchport, name='edit_switchport'),

    path('add_switchport/', 
        views.add_or_edit_switchport, name='add_switchport'),

    path('edit_aka/<int:pk>/<slug:slug>/', 
        views.add_or_edit_aka, name='edit_aka'),

    path('add_aka/', 
        views.add_or_edit_aka, name='add_aka'),

    path('ajax/load-ports/', views.ajax_load_ports, name='ajax_load_ports')

    
]