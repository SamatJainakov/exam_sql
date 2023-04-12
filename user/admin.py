from django.contrib import admin
from .models import Language, Student, Mentor, Course


@admin.register(Language)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'month_to_learn']
    search_fields = ['name', ]


@admin.register(Student)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['work_study_place', 'has_own_notebook', 'preferred_os']
    search_fields = ['work_study_place', 'preferred_os']


@admin.register(Mentor)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['main_work', 'experience']
    search_fields = ['main_work', ]


@admin.register(Course)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'language', 'date_started', 'mentor', 'student']
    search_fields = ['name', 'language']
