from django.contrib import admin

from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    list_per_page = 10

admin.site.register(Teacher, TeacherAdmin)
