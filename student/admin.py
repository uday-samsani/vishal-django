from django.contrib import admin

# Register your models here.

from .models import StudentInfo

@admin.register(StudentInfo)

class StudentInfoAdmin(admin.ModelAdmin):
    list_display=["name","stream","year"]