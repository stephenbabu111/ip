from django.contrib import admin

from .models import login_table,ip_table

admin.site.register(login_table)
admin.site.register(ip_table)
