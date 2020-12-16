from django.contrib import admin
from .models import Organisation, POP, PortConnection, Fee
from core.utils import generate_random_string

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(PortConnection)
admin.site.register(POP)
admin.site.register(Fee)