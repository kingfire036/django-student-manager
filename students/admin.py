from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'enrollment_number', 'date_of_birth', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'enrollment_number')
    list_filter = ('date_of_birth', 'created_at')