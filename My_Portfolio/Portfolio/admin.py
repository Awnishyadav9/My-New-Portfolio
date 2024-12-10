from django.contrib import admin
from .models import QueryData

class Authoradmin(admin.ModelAdmin):
    list_display = ['name','user_email','user_query']

admin.site.register(QueryData,Authoradmin)
