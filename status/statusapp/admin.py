from django.contrib import admin

from statusapp.models import * 

@admin.register(Contact_Us)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','mobile_no','message']
