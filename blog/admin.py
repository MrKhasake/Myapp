from django.contrib import admin
from .models import Entrepreneurship, Sales, Finance

# Register your models here.
class EntreAdmin(admin.ModelAdmin):
    list_display = ['title','category','writer','Create_at']
    list_filter = ['category', 'Create_at', 'writer']
    search_fields = ['title', 'header', 'body']



class FinAdmin(admin.ModelAdmin):
    list_display = ['title','category','writer','Create_at']
    list_filter = ['category', 'Create_at', 'writer']
    search_fields = ['title', 'header', 'body']

admin.site.register(Entrepreneurship, EntreAdmin)
admin.site.register(Sales, SaleAdmin)
admin.site.register(Finance, FinAdmin)