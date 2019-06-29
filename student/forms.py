from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Marklist, Syllabus, CustomUser
import datetime

from django.contrib.auth import get_user_model
from django.conf import settings

User1 = settings.AUTH_USER_MODEL


# User1=get_user_model();
# used to create the blueprint of the form for registering users that use the site
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'dept', 'password1', 'groups']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'dept']


class Userform(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'dept', 'password1', 'groups']
        exclude = ('password1', 'password',)

    def __init__(self, *args, **kwargs):
        super(Userform, self).__init__(*args, **kwargs)
        self.fields['dept'].widget.attrs['style'] = 'width:320px;'
        self.fields['groups'].widget.attrs['style'] = 'width:150px;height:100px'
        self.fields['groups'].label = 'Category'
        self.fields['dept'].label = 'Department'
        self.fields['email'].widget.attrs['style'] = 'width:320px;'
        self.fields['first_name'].widget.attrs['style'] = 'width:200px;'
        self.fields['last_name'].widget.attrs['style'] = 'width:200px;'
        self.fields['username'].widget.attrs['style'] = 'width:200px;'
        self.fields['password1'].widget.attrs['style'] = 'width:200px;'
        self.fields['password2'].widget.attrs['style'] = 'width:200px;'


def save(self, commit=True):
    user = super(UserCreationForm, self).save(commit=False)
    # user.accesslvl = self.cleaned_data['accesslvl']

    if commit:
        user.save()

    return user


class LoginUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        exclude = ('password1', 'password2',)

    def save(self, commit=True):
        user = super(LoginUser, self).save(commit=False)
        # user.accesslvl = self.cleaned_data['accesslvl']

        if commit:
            user.save()

        return user


# class LoginForm(forms.ModelForm):
from .models import Student


class StudentForm(forms.ModelForm):
    CHANCES = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))

    # id = forms.IntegerField(disabled=True,required=False)
    regno = forms.IntegerField(disabled=True, widget=forms.TextInput(attrs={'size': 2}),
                               required=False)  # to make read only
    cursem = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 1}), required=False)
    section = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 1}), required=False)
    chance = forms.ChoiceField(choices=CHANCES, widget=forms.TextInput(attrs={'size': 1}), required=False)

    subcode1 = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}), required=False)
    # subcode3 = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}))
    subcode2 = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}), required=False)
    subcode3 = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}), required=False)
    subcode4 = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}), required=False)
    subcode5 = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}), required=False)
    subcode6 = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}), required=False)
    subcodel1 = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}), required=False)
    subcodel2 = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}), required=False)
    subcodel3 = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}), required=False)
    subcodel4 = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}), required=False)

    mark1 = forms.IntegerField(widget=forms.TextInput(attrs={'size': 1}), required=False)
    mark2 = forms.IntegerField(widget=forms.TextInput(attrs={'size': 1}), required=False)
    mark3 = forms.IntegerField(widget=forms.TextInput(attrs={'size': 1}), required=False)
    mark4 = forms.IntegerField(widget=forms.TextInput(attrs={'size': 1}), required=False)
    mark5 = forms.IntegerField(widget=forms.TextInput(attrs={'size': 1}), required=False)
    mark6 = forms.IntegerField(widget=forms.TextInput(attrs={'size': 1}), required=False)
    markl1 = forms.IntegerField(widget=forms.TextInput(attrs={'size': 1}), required=False)
    markl2 = forms.IntegerField(widget=forms.TextInput(attrs={'size': 1}), required=False)
    markl3 = forms.IntegerField(widget=forms.TextInput(attrs={'size': 1}), required=False)
    markl4 = forms.IntegerField(widget=forms.TextInput(attrs={'size': 1}), required=False)

    class Meta:
        model = Marklist
        # fields = '__all__'
        # exclude = ['regno','branch','cursem','section','type']
        exclude = ('id',)
        # read_only = ['regno', ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # self.fields['id'].required = False
        # self.fields['regno'].queryset = Marklist.objects.filter(branch=self.request.user.dept)
        # instance = ge
        # tattr(self, 'instance', None)


# from dal import autocomplete
class MarklistForm(forms.ModelForm):
    # branch = models.CharField(max_length=70, choices=BRANHCES)
    BRANCHES = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
                ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
                ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
                ('ME', 'Mechanical Engineering'))

    regno = forms.ModelChoiceField(disabled=True,queryset=Student.objects.all())

    class Meta:
        model = Marklist
        fields = '__all__'
        exclude = ['branch']

    def __init__(self, *args, **kwargs):
        super(MarklistForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        # self.user = kwargs.pop('user',None)
        # print("++++++++++++++ ",self.user.dept)
        # dept = self.user.dept

        # self.fields['regno'].queryset = Student.objects.filter(branch=dept)
        # self.fields['branch'].value =dept
        self.fields['regno'].widget.attrs['style'] = 'width:250px;'
        # self.fields['sub1'].widget.attrs['style'] = 'width:400px;'
        # self.fields['sub2'].widget.attrs['style'] = 'width:400px;'
        # self.fields['sub3'].widget.attrs['style'] = 'width:400px;'
        # self.fields['sub4'].widget.attrs['style'] = 'width:400px;'
        # self.fields['sub5'].widget.attrs['style'] = 'width:400px;'
        # self.fields['sub6'].widget.attrs['style'] = 'width:400px;'
        # self.fields['subl1'].widget.attrs['style'] = 'width:400px;'
        # self.fields['subl2'].widget.attrs['style'] = 'width:400px;'
        # self.fields['subl3'].widget.attrs['style'] = 'width:400px;'
        # self.fields['subl4'].widget.attrs['style'] = 'width:400px;'

        self.fields['regno'].label = 'Register Number'
        self.fields['type'].label = 'Exam Type'
        self.fields['join'].label = 'Year of Join'
        self.fields['subcodel1'].label = 'Lab1 Name'
        self.fields['subcodel2'].label = 'Lab2 Name'
        self.fields['subcodel3'].label = 'Lab3 Name'
        self.fields['subcodel4'].label = 'Lab4 Name'
        self.fields['cursem'].label = 'Semester'


class Studentmodelform(forms.ModelForm):
    EXAM_YEAR = []
    end_limit = datetime.datetime.today().year + 1
    start_limit = datetime.datetime.today().year - 4

    for x in range(start_limit, end_limit):
        EXAM_YEAR.append((x, x))

    name = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+'}), label='Name')
    dateofbirth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    qualifyingyear = forms.CharField(widget=forms.Select(choices=EXAM_YEAR), label='Qualifying Year')
    tenyear = forms.CharField(widget=forms.Select(choices=EXAM_YEAR), label='10th Qualifying Year')
    permanentaddress = forms.CharField(widget=forms.Textarea())
    temporaryaddress = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['branch']

    def __init__(self, *args, **kwargs):
        super(Studentmodelform, self).__init__(*args, **kwargs)
        self.fields['permanentaddress'].widget.attrs['style'] = 'width:400px;height:180px'
        self.fields['temporaryaddress'].widget.attrs['style'] = 'width:400px;height:180px'
        self.fields['status'].widget.attrs['style'] = 'width:200px;'
        self.fields['category'].widget.attrs['style'] = 'width:250px;'
        self.fields['emailid'].widget.attrs['style'] = 'width:250px;'
        self.fields['personwithdisabilities'].widget.attrs['style'] = 'width:250px;'
        self.fields['religion'].widget.attrs['style'] = 'width:200px;'
        self.fields['parentorguardianname'].widget.attrs['style'] = 'width:250px;'
        self.fields['parentorguardianoccupation'].widget.attrs['style'] = 'width:250px;'
        self.fields['parentorguardiancontactno'].widget.attrs['style'] = 'width:250px;'
        self.fields['parentorguardianemailid'].widget.attrs['style'] = 'width:250px;'
        self.fields['miniproject'].widget.attrs['style'] = 'width:250px;'
        self.fields['mainproject'].widget.attrs['style'] = 'width:250px;'
        self.fields['mainprojectguide'].widget.attrs['style'] = 'width:250px;'
        self.fields['studentcontactno'].widget.attrs['style'] = 'width:150px;'
        self.fields['miniprojectguide'].widget.attrs['style'] = 'width:250px;'
        self.fields['studentemailid'].widget.attrs['style'] = 'width:250px;'
        self.fields['tenboard'].widget.attrs['style'] = 'width:250px;'
        self.fields['tenregisterno'].widget.attrs['style'] = 'width:250px;'
        self.fields['tenmarks'].widget.attrs['style'] = 'width:250px;'
        self.fields['tenpercentage'].widget.attrs['style'] = 'width:250px;'
        self.fields['tenyear'].widget.attrs['style'] = 'width:250px;'
        self.fields['tenyear'].label = '10th Year of Passout'
        self.fields['qualifyingboard'].widget.attrs['style'] = 'width:250px;'
        self.fields['qualifyingregisterno'].widget.attrs['style'] = 'width:250px;'
        self.fields['qualifyingmarks'].widget.attrs['style'] = 'width:250px;'
        self.fields['qualifyingpercentage'].widget.attrs['style'] = 'width:250px;'
        self.fields['qualifyingyear'].widget.attrs['style'] = 'width:250px;'
        self.fields['specialreservation'].widget.attrs['style'] = 'width:250px;'
        self.fields['emailid'].widget.attrs['style'] = 'width:250px;'
        self.fields['name'].widget.attrs['style'] = 'width:250px;'

        self.fields['name'].label = 'Student Name'
        self.fields['cursem'].label = 'Semester'
        self.fields['join'].label = 'Year of Join'
        self.fields['admtype'].label = 'Admission Type'
        self.fields['permanentaddress'].label = 'Permanent Address'
        self.fields['temporaryaddress'].label = 'Temporary Address'
        self.fields['dateofbirth'].label = 'Date of Birth'
        # self.fields['parentorguardianname'].label = 'Parent/Guardian Name'
        # self.fields['parent'].label = 'Parent Name'

        # self.fields['regno'].queryset = Student.objects.filter(branch=self.request.user.dept)


class Studentupdateform(forms.ModelForm):
    regno = forms.IntegerField(disabled=True, widget=forms.TextInput(attrs={'size': 2}))
    name = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3, 'pattern': '[A-Za-z]+'}))
    join = forms.IntegerField(disabled=True, widget=forms.TextInput(attrs={'size': 3}))
    admtype = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 3}))

    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Studentupdateform, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['style'] = 'width:180px;'
        self.fields['branch'].widget.attrs['style'] = 'width:320px;'
        self.fields['regno'].label = 'Register Number'
        self.fields['name'].label = 'Student Name'
        self.fields['cursem'].label = 'Semester'
        self.fields['join'].label = 'Year of Join'
        self.fields['admtype'].label = 'Admission Type'
        # self.fields['parent'].label = 'Parent Name'


class MarklistUpdateForm(forms.ModelForm):
    # branch = models.CharField(max_length=70, choices=BRANHCES)
    BRANCHES = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
                ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
                ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
                ('ME', 'Mechanical Engineering'))

    class Meta:
        model = Marklist
        fields = '__all__'
        exclude = ['branch']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(MarklistUpdateForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        if self.instance:
            self.fields['regno'].queryset = Marklist.objects.filter(cursem=self.instance.cursem)

        # self.user = kwargs.pop('user',None)
        # print("++++++++++++++ ",self.user.dept)
        # dept = self.request.user.dept

        # self.fields['regno'].queryset = Student.objects.filter(branch=dept)
        # self.fields['branch'].value =dept
        self.fields['regno'].widget.attrs['style'] = 'width:250px;'
        # self.fields['sub1'].widget.attrs['style'] = 'width:400px;'
        # self.fields['sub2'].widget.attrs['style'] = 'width:400px;'
        # self.fields['sub3'].widget.attrs['style'] = 'width:400px;'
        # self.fields['sub4'].widget.attrs['style'] = 'width:400px;'
        # self.fields['sub5'].widget.attrs['style'] = 'width:400px;'
        # self.fields['sub6'].widget.attrs['style'] = 'width:400px;'
        # self.fields['subl1'].widget.attrs['style'] = 'width:400px;'
        # self.fields['subl2'].widget.attrs['style'] = 'width:400px;'
        # self.fields['subl3'].widget.attrs['style'] = 'width:400px;'
        # self.fields['subl4'].widget.attrs['style'] = 'width:400px;'

        self.fields['regno'].label = 'Register Number'
        self.fields['type'].label = 'Exam Type'
        self.fields['join'].label = 'Year of Join'
        self.fields['subcodel1'].label = 'Lab1 Name'
        self.fields['subcodel2'].label = 'Lab2 Name'
        self.fields['subcodel3'].label = 'Lab3 Name'
        self.fields['subcodel4'].label = 'Lab4 Name'
        self.fields['cursem'].label = 'Semester'


class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SyllabusForm, self).__init__(*args, **kwargs)
        self.fields['dept'].widget.attrs['rows'] = 20


class Syllabusmodelform(forms.ModelForm):
    EXAM_YEAR = []
    end_limit = datetime.datetime.today().year + 1
    start_limit = datetime.datetime.today().year - 2

    for x in range(start_limit, end_limit):
        EXAM_YEAR.append((x, x))

    year = forms.CharField(widget=forms.Select(choices=EXAM_YEAR))

    class Meta:
        model = Syllabus
        fields = '__all__'
        exclude = ['dept']

    def __init__(self, *args, **kwargs):
        super(Syllabusmodelform, self).__init__(*args, **kwargs)
        self.fields['year'].label = 'Year Of Syllabus'


class Syllabusupdateform(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Syllabusupdateform, self).__init__(*args, **kwargs)
        # self.fields['status'].widget.attrs['style'] = 'width:180px;'
        self.fields['dept'].widget.attrs['style'] = 'width:320px;'


from .models import Faculty


class Facultymodelform(forms.ModelForm):
    # dob = forms.DateField(input_formats=DATE_INPUT_FORMATS, help_text='dd-mm-yyyy')

    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    datejoin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    dateresig = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    ename = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+'}), label='Name')

    class Meta:
        model = Faculty
        fields = '__all__'
        exclude = ('dateresig', 'dept',)

    def __init__(self, *args, **kwargs):
        super(Facultymodelform, self).__init__(*args, **kwargs)
        self.fields['ename'].widget.attrs['style'] = 'width:280px;'
        self.fields['desig'].widget.attrs['style'] = 'width:200px;'
        self.fields['ename'].widget.attrs['style'] = 'width:280px;'
        self.fields['permaddr'].widget.attrs['style'] = 'width:400px;height:150px'
        self.fields['tempaddr'].widget.attrs['style'] = 'width:400px;height:150px'
        self.fields['email'].widget.attrs['style'] = 'width:300px;'
        self.fields['permaddr'].label = 'Permenant Address'
        self.fields['tempaddr'].label = 'Temporary Address'
        self.fields['dob'].label = 'Date Of Birth'
        self.fields['datejoin'].label = 'Date Of Join'
        self.fields['dateresig'].label = 'Date Of Resignation'
        self.fields['empid'].label = 'Faculty ID'
        self.fields['contact'].label = 'Contact Number'

        self.fields['dateresig'].required = False
        # self.fields['dateresig'].widget = forms.HiddenInput()
        # self.fields['dateresig'].


# uppload student login credentials
class UserCsvForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'dept', 'password', 'email', ]
        # exclude = ['password2']


class StudentCsvForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ('photo',)


from .models import RollnoRegnoMap


class MarklistCsvform(forms.ModelForm):
    subcode5 = forms.CharField(required=False)
    mark5 = forms.IntegerField(required=False)

    class Meta:
        model = Marklist
        fields = '__all__'
        exclude = ('id',)


class FacultyCsvform(forms.ModelForm):
    # datejoin = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'))

    class Meta:
        model = Faculty
        fields = '__all__'
        exclude = ('dateresig','datejoin')


class AttendenceCsvForm(forms.ModelForm):
    class Meta:
        model = RollnoRegnoMap
        fields = '__all__'
        exclude = ('id', 'time', 'atotal', 'ptotal', 'ftotal')

    def __init__(self, *args, **kwargs):
        super(AttendenceCsvForm, self).__init__(*args, **kwargs)
        self.fields['rollno'].widget.attrs['style'] = 'width:50px;'
        self.fields['name'].widget.attrs['style'] = 'width:100px;'


from .models import Subject_Profile


class SubjectProfileAddForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'style': 'text-transform:uppercase;'}))

    class Meta:
        model = Subject_Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SubjectProfileAddForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['style'] = 'width:320px;'
        self.fields['branch'].widget.attrs['style'] = 'width:320px;'
        self.fields['code'].widget.attrs['style'] = 'width:120px;'
        self.fields['name'].label = 'Subject Name'
        self.fields['code'].label = 'Subject Code'
        self.fields['branch'].label = 'Branch'
        self.fields['sem'].label = 'Semester'
        self.fields['stype'].label = 'Subject Type'
        self.fields['credit'].label = 'Credit'


from .models import FacultySubject


class FacultySubjectMapAddForm(forms.ModelForm):
    class Meta:
        model = FacultySubject
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FacultySubjectMapAddForm, self).__init__(*args, **kwargs)
        self.fields['branch'].widget.attrs['style'] = 'width:320px;'
        self.fields['empid'].widget.attrs['style'] = 'width:150px;'
        self.fields['empid'].label = 'Faculty ID'
        self.fields['year'].label = 'Syllabus Year'


class SubjectProfileForm(forms.ModelForm):
    class Meta:
        model = Subject_Profile
        fields = '__all__'


from .models import RollnoRegnoMap


class RollnoRegnoMapEditForm(forms.ModelForm):
    facultyid = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'size': 5}), required=False)
    # id = forms.IntegerField(disabled=True, required=True)
    # rollno = forms.IntegerField(disabled=True)
    name = forms.CharField(disabled=True)
    # time = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'))
    subjectcode = forms.CharField(disabled=True)

    class Meta:
        model = RollnoRegnoMap
        # fields = ['rollno', 'name', 'firsthr', 'secondhr', 'thirdhr', 'fourthhr', 'fifthhr', 'sixthhr',]
        fields = ('rollno', 'name', 'firsthr', 'secondhr', 'thirdhr',
                  'fourthhr', 'fifthhr', 'sixthhr', 'facultyid','subjectcode')
        exclude = ('time', 'id',)

    def __init__(self, *args, **kwargs):
        super(RollnoRegnoMapEditForm, self).__init__(*args, **kwargs)
        self.fields['rollno'].widget.attrs['style'] = 'width:40px;'
        # self.fields['id'].widget = forms.HiddenInput()
        # self.fields['branch'].widget.attrs['style'] = 'width:320px;'


class RollnoRegnoMapAddForm(forms.ModelForm):
    class Meta:
        model = RollnoRegnoMap
        fields = '__all__'
