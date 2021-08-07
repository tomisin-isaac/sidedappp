from django.contrib import admin
from.models import *

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','message','status','notes')
    readonly_fields = ('name','email','message')
    list_filter = ['status']
    list_display_links = ('status','name','notes')
    search_fields = ('name','email','subject','message','status','notes')
    list_per_page = 20
# Register your models here.
admin.site.register(Setting)
admin.site.register(ContactMessage,ContactMessageAdmin)
admin.site.register(Images)