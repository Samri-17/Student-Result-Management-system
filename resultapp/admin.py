from django.contrib import admin

# Register your models here.
from .models import Class, Subject, Student, SubjectCombination, Result

admin.site.register(Class)
admin.site.register(Subject)            
admin.site.register(Student)
admin.site.register(SubjectCombination)
admin.site.register(Result)