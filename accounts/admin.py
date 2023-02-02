from django.contrib import admin
from .models import Student, Lecturer


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = ['registration_number', 'first_name', 'last_name']
    ordering = ['user__first_name', 'user__last_name']
    autocomplete_fields = ['user', 'department']


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'first_name', 'last_name']
    ordering = ['user__first_name', 'user__last_name']
    autocomplete_fields = ['user', 'department']
