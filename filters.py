from .models import *
import django_filters


class AttendenceFilter(django_filters.FilterSet):
    facultyid = django_filters.ModelMultipleChoiceFilter(queryset=Faculty.objects.all())
    subjectcode = django_filters.ModelMultipleChoiceFilter(queryset=Subject_Profile.objects.all())
    time = django_filters.DateFromToRangeFilter()
    class Meta:
        model = RollnoRegnoMap
        fields = ['regno', 'cursem', 'section', 'facultyid', 'subjectcode','time']


class MarklistFilter(django_filters.FilterSet):
    class Meta:
        model = Marklist
        fields = ['type','regno', 'branch', 'cursem','chance']


class StudentDetailFilter(django_filters.FilterSet):
    dateofbirth = django_filters.DateFilter(input_formats=['%d-%m-%Y'])

    class Meta:
        model = Student
        fields = ['regno', 'dateofbirth', 'branch', ]


class StudentFilter(django_filters.FilterSet):
    # regno = django_filters.NumberFilter(lookup_expr='icontains')
    dateofbirth = django_filters.DateFilter(input_formats=['%d-%m-%Y'])

    class Meta:
        model = Student
        fields = ['cursem', 'join', 'regno', 'dateofbirth', 'branch']


class FacultyFilter(django_filters.FilterSet):
    class Meta:
        model = Faculty
        fields = ['ename', 'desig', 'category']


class SyllabusFilter(django_filters.FilterSet):
    class Meta:
        model = Syllabus
        fields = ['year', ]


class FacultySubjectFilter(django_filters.FilterSet):
    class Meta:
        model = FacultySubject
        fields = ['branch', 'sem', 'subcode']
