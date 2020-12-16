from django.urls import path

from . import views

urlpatterns = [

	#path('<int:story_id>/', views.story, name='story'),
    path('pop/<int:pk>/<slug:slug>/', views.edit_pop, name='edit_pop'),
    path('organisation/<int:pk>/<slug:slug>/', views.edit_organisation, name='edit_organisation'),
    path('port_connection/<int:pk>/<slug:slug>/', views.edit_port_connection, name='edit_port_connection'),
    path('port_charge/<int:pk>/<slug:slug>/', views.edit_port_charge, name='edit_port_charge'),
    path('add_pop/', views.add_pop, name='add_pop'),
    path('add_port_charge/', views.add_port_charge, name='add_port_charge'),
    path('add_organisation/', views.add_organisation, name='add_organisation'),
    path('add_port_connection/', views.add_port_connection, name='add_port_connection'),
	path('', views.home, name='home'),
    
	#path('addstory/', views.addstory, name='addstory'),
	#path('addstory/<int:story_id>/', views.addstory, name='addstory'),
	#path('editstory/<int:story_id>/', views.editstory, name='editstory'),
]