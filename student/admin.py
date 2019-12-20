from django.contrib import admin
# Register your models here.
from .models import Student, Subject_Profile, Faculty, FacultySubject, Syllabus,Marklist
from .models import *
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
admin.site.site_url='/student/'



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username']#,'email','dept']
    # add_fieldsets = 'dept'


class StudentAdmin(admin.ModelAdmin):
    # readonly_fields = ('regno','name','join')
    fields = ('photo', 'regno', 'name', 'branch', 'cursem', 'join', 'section', 'status')


class FacultySubMap(admin.StackedInline):
    model = FacultySubject
    extra = 0
    autocomplete_fields = ('empid',)

class MarklistAdmin(admin.ModelAdmin):
    list_filter = ('branch','cursem','type',)
    autocomplete_fields = ('regno',)
    list_display = ('regno','cursem','branch','type')
    search_fields = ['regno__id',]

# admin.site.register(Marklist,MarklistAdmin)

class FacultySubjectAdmin(admin.ModelAdmin):
    list_display = ('empid', 'ename', 'dept')
    search_fields = ('empid',)
    list_filter = ('dept',)
    # autocomplete_fields = ('empid',)

    inlines = [FacultySubMap]


class FacultySubjectMapAdmin(admin.ModelAdmin):
    autocomplete_fields = ('empid',)

admin.site.register(CustomUser,CustomUserAdmin)


admin.site.register(Faculty, FacultySubjectAdmin)

admin.site.register(Syllabus)
# admin.site.register(Subject_Profile)
admin.site.register(FacultySubject, FacultySubjectMapAdmin)

# for import export functionality in admin page

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.models import UserManager,Group


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    list_display = ('regno','name','cursem','branch','status')
    search_fields = ('regno','name')
    list_filter = ('branch','cursem','status')
    list_per_page = 10


class Subject_ProfileResource(resources.ModelResource):
    class Meta:
        model = Subject_Profile


@admin.register(Subject_Profile)
class Subject_ProfileAdmin(ImportExportModelAdmin):
    resource_class = Subject_ProfileResource
    list_display = ('syllabussubid', 'code','name', 'sem')
    search_fields = ('syllabussubid', 'name','code')
    list_filter = ('branch', 'sem')
    list_per_page = 10
    # autocomplete_fields = ('syllabussubid',)

admin.site.register(Marklist,MarklistAdmin)

# admin.site.register(StudentFacultyLabMap)
#
# admin.site.register(RollnoRegnoMap)


# from .models import Contact
#
# admin.site.register(Contact)
