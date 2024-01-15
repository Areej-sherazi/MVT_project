from django.contrib import admin
from .models import students
# Register your models here.

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'grade')
admin.site.register(students, StudentAdmin)

