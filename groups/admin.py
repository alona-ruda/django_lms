from django.contrib import admin

from .models import Group

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'headman', 'start_date', 'end_date')
    list_per_page = 5


admin.site.register(Group, GroupAdmin)
