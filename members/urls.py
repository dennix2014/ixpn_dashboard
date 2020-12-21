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
    
]