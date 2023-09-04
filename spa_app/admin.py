from django.contrib import admin
from .models import Visitor,StaffMember,VisitorDetails,Drink,VisitorDrink
# Register your models here.

class VisitorAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','address']

admin.site.register(Visitor,VisitorAdmin)

class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ['name','image','email','mobile']

admin.site.register(StaffMember,StaffMemberAdmin)