from django.contrib import admin

from core.models import Student, StudentProfile, Course, Teacher

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(Course)
admin.site.register(Teacher)