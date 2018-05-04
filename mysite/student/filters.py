from .models import Student, Faculty,Syllabus
import django_filters


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['branch', 'cursem', 'join']


class FacultyFilter(django_filters.FilterSet):
    class Meta:
        model = Faculty
        fields = ['dept', 'desig', 'category']


class SyllabusFilter(django_filters.FilterSet):
    class Meta:
        model = Syllabus
        fields=['year','dept']

