from django.contrib import admin
from .models import Member, POP, PortConnection
from core.utils import generate_random_string

class MemberAdmin(admin.ModelAdmin):
    list_display = ('short_name',)
    prepopulated_fields = {'slug': ('short_name',)}

# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(PortConnection)
admin.site.register(POP)