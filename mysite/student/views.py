from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render, get_list_or_404, get_object_or_404

from django.urls import reverse_lazy

from django.http import HttpResponse

from .models import Subject_Profile, FacultySubject,Student,Faculty,Marklist

from django.contrib.auth.models import User
# for user forms (4 imports)
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import Userform


def home(request):
    return render(request,'student/home.html')




def testing(request):
    return render(request, 'student/base_new.html')


class Indexview(generic.ListView):
    template_name = 'student/home.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Student.objects.all()


class DetailView(generic.DetailView):
    model = Student
    template_name = 'student/student_detail.html'
    context_object_name = 'object_list'


# prints student details
def detail(request, regno):
    list = get_list_or_404(Student, pk=regno)
    marklist=get_list_or_404(Marklist,regno=regno)


    context = {'list': list,
               'marks':marklist,
               }
    return render(request, 'student/detail.html', context)


class Studentcreate(CreateView):
    model = Student
    fields = ['photo', 'regno', 'name', 'branch', 'cursem', 'join', 'section']
    success_url = reverse_lazy('student:index')


class Studentupdate(UpdateView):
    model = Student
    fields = ['photo', 'name', 'branch', 'cursem', 'join', 'section']
    success_url = reverse_lazy('student:index')


class Studentdelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student:index')


# form code below


def searchs(request):
    if request.method == 'GET':
        if 'regno' in request.GET or 'name in request.GET' or 'branch in request.GET':
            num = request.GET['regno']
            name = request.GET['name']
            branch = request.GET['branch']
            student = Student.objects.filter(regno__icontains=num, name__icontains=name, branch__icontains=branch)
            context = {'list': student, }

            message = 'You searched for ', request.GET['regno']
            return render(request, 'student/detail.html', context)

        else:
            message = 'You submitted an empty form'

    return HttpResponse(message)


def Studentsearch(request):
    # searchs(request)
    return render(request, 'student/search_student.html')


class UserFormView(View):
    form_class = Userform
    template_name = 'student/register_user.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaning the input data from user

            username = form.cleaned_data['username']

            password = form.cleaned_data['password']

            #accesslvl = form.cleaned_data['accesslvl']

            user.set_password(password)
            user.save()

            # to login the user with username and password
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                    return redirect('student:home')

        return render(request, self.template_name, {'form': form})
       # context = {'list': user, }
       # return render(request, 'student/account_created.html', context)


from .models import Student
from .filters import StudentFilter


def student_search(request):
   if request.method == 'GET':
        student_list = Student.objects.all()
        student_filter = StudentFilter(request.GET, queryset=student_list)
        print("student ")
        return render(request, 'student/student_list.html', {'filter': student_filter})


# for faculty only

from .models import Faculty
from .filters import FacultyFilter


def faculty_search(request):
    faculty_list = Faculty.objects.all()
    faculty_filter = FacultyFilter(request.GET, queryset=faculty_list)
    return render(request, 'student/faculty_list.html', {'filter': faculty_filter})


class Facultyview(generic.ListView):
    template_name = 'student/facultyindex.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Faculty.objects.all()


def FacultyDetail(request, empid):
    list = get_list_or_404(Faculty, pk=empid)

    context = {'list': list, }
    return render(request, 'student/facultydetail.html', context)


class FacultyCreate(CreateView):
    model = Faculty
    fields = '__all__'
    success_url = reverse_lazy('student:faculty_show')


class Facultyupdate(UpdateView):
    model = Faculty
    fields = '__all__'
    success_url = reverse_lazy('student:faculty_show')


class Facultydelete(DeleteView):
    model = Faculty
    success_url = reverse_lazy('student:faculty_show')


# for subjects


def SubjectsList(request):
    sublist = Subject_Profile.objects.all()
    context = {'list': sublist, }
    return render(request, 'student/subjectdetail.html', context)


# facultysubject map

class FacultySubMapview(generic.ListView):
    template_name = 'student/facultysubmapindex.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return FacultySubject.objects.all()


class FacultySubMapCreate(CreateView):
    model = FacultySubject
    fields = '__all__'
    success_url = reverse_lazy('student:faculty_show')


class FacultySubMapEdit(UpdateView):
    model = FacultySubject
    fields = '__all__'
    success_url = reverse_lazy('student:faculty_show')


# for marklist

from .models import Marklist


class MarklistCreate(CreateView):
    model = Marklist
    fields = '__all__'
    success_url = reverse_lazy('student:index')


class MarklistUpdate(UpdateView):
    model = Marklist
    fields = '__all__'
    success_url = reverse_lazy('student:index')


from .models import Subject_Profile

class Subject_ProfileCreate(CreateView):
    model = Subject_Profile
    fields = '__all__'
    success_url = reverse_lazy('student:index')

class Subject_ProfileEdit(UpdateView):
    model = Subject_Profile
    fields = '__all__'
    success_url = reverse_lazy('student:index')


#syllabus

from .models import Syllabus


from .filters import SyllabusFilter

def syllabus_search(request):
    syllabus_list = Faculty.objects.all()
    syllabus_filter = FacultyFilter(request.GET, queryset=syllabus_list)
    return render(request, 'student/ayllabus_list.html', {'filter': syllabus_filter})





class SyllabusCreate(CreateView):
    model = Syllabus
    fields = '__all__'
    success_url = reverse_lazy('student:index')

class SyllabusEdit(UpdateView):
    model = Syllabus
    fields = '__all__'
    success_url = reverse_lazy('student:index')

def SyllabusDetail(request, regno):
    list = get_list_or_404(Syllabus, pk=regno)
    # marklist=get_list_or_404(Marklist,pk=regno)

    context = {'list': list,

               }
    return render(request, 'student/syllabus_detail.html', context)