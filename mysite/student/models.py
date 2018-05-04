from django.db import models
from django.urls import reverse


# for each table created here in models perform the following commands
#    1. python manage.py makemigrations <app_name>
#    2. python manage.py migrate


# Create your models here.

def upload_location(instance, filename):
    return "student/%s/%s" % (instance.regno, filename)


class Student(models.Model):  # Have to add all 42 fields this will be done at last
    SECTION = (('A', 'A'), ('B', 'B'))

    BRANHCES = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
                ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
                ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
                ('ME', 'Mechanical Engineering'))

    SEMESTERS = (('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'),
                 ('8', 'S8'))

    STATUS = (('Active', 'Currently Studying'), ('Pass out', 'Course Completed'),
              ('Drop out', 'Drop out '))

    YEARS = (tuple((x, x)) for x in range(2015, 2050))

    ADM = (('Regular','Regular'),('Lateral Entry','Lateral Entry'))

    photo = models.FileField(upload_to=upload_location, null=True, blank=True)
    regno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=15, choices=BRANHCES)
    cursem = models.CharField(max_length=2, choices=SEMESTERS)
    join = models.IntegerField(choices=YEARS)
    section = models.CharField(max_length=1, choices=SECTION)
    status = models.CharField(max_length=20, choices=STATUS, default='Active')
    parent = models.CharField(max_length=20)
    admtype=models.CharField(max_length=20,choices=ADM,default='Regular')

    # after adding data to the database this func is called to redirect to the homepage
    def get_absolute_url(self):
        return reverse('student:index', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.regno) + ' ' + self.name

    class Meta:
        ordering = ('regno',)


class Syllabus(models.Model):
    DEPT = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
            ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication Engineering'),
            ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
            ('ME', 'Mechanical Engineering'))

    YEARS = (tuple((x, x)) for x in range(2015, 2050))

    year = models.PositiveIntegerField(choices=YEARS)
    dept = models.CharField(max_length=60, choices=DEPT)
    theory_no = models.PositiveIntegerField()
    max_internal = models.PositiveIntegerField()
    max_external = models.PositiveIntegerField()
    lab_no = models.PositiveIntegerField()
    max_lab_external = models.PositiveIntegerField()
    max_miniproj = models.PositiveIntegerField()
    max_mainproj = models.PositiveIntegerField()

    def __str__(self):
        return self.dept + '_' + str(self.year)


class Subject_Profile(models.Model):
    SUB_TYPES = (('T', 'Theory'), ('L', 'Practical'), ('P', 'Project'))

    BRANCHES = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
                ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
                ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
                ('ME', 'Mechanical Engineering'))

    SEMESTERS = (('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'),
                 ('8', 'S8'))

    syllabussubid = models.ForeignKey(Syllabus, on_delete=models.CASCADE, default='1')
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=70)
    branch = models.CharField(max_length=70, choices=BRANCHES)
    sem = models.CharField(max_length=2, choices=SEMESTERS)
    stype = models.CharField(max_length=15, choices=SUB_TYPES)
    credit = models.IntegerField(default=3)

    def __str__(self):
        return self.code + '   ' + self.name

    class Meta:
        ordering = ('sem',)


class Marklist(models.Model):
    SECTION = (('A', 'A'), ('B', 'B'))

    BRANHCES = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
                ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
                ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
                ('ME', 'Mechanical Engineering'))

    SEMESTERS = (('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'),
                 ('8', 'S8'))

    EXAMS = (('Internal', 'Internal'), ('External', 'External'))

    CHANCES = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))

    regno = models.ForeignKey(Student, on_delete=models.CASCADE)
    branch = models.CharField(max_length=70, choices=BRANHCES)
    cursem = models.CharField(max_length=2, choices=SEMESTERS)
    section = models.CharField(max_length=1, choices=SECTION)
    type = models.CharField(max_length=9, choices=EXAMS,default='Internal')

    sub1 = models.CharField(max_length=60, default='0')
    mark1 = models.SmallIntegerField(default='0')
    sub2 = models.CharField(max_length=60, default='0')
    mark2 = models.SmallIntegerField(default='0')
    sub3 = models.CharField(max_length=60, default='0')
    mark3 = models.SmallIntegerField(default='0')
    sub4 = models.CharField(max_length=60, default='0')
    mark4 = models.SmallIntegerField(default='0')
    sub5 = models.CharField(max_length=60, default='0')
    mark5 = models.SmallIntegerField(default='0')
    sub6 = models.CharField(max_length=60, default='0')
    mark6 = models.SmallIntegerField(blank=True, default='0')
    subl1 = models.CharField(max_length=60, default='0')
    markl1 = models.SmallIntegerField(default='0')
    subl2 = models.CharField(max_length=60, default='0')
    markl2 = models.SmallIntegerField(default='0')
    subl3 = models.CharField(max_length=60, null=True, blank=True)
    markl3 = models.SmallIntegerField(blank=True, default='0')
    subl4 = models.CharField(max_length=60, null=True, blank=True)
    markl4 = models.SmallIntegerField(blank=True, default='0')

    def __str__(self):
        return str(self.regno.regno) + ' ' + str(self.regno.name) + ' S' + str(self.cursem)

    class Meta:
        ordering = ('cursem',)


def upload_location(instance, filename):
    return "faculty/%s/%s" % (instance.empid, filename)


class Faculty(models.Model):
    DEPT = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
            ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
            ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
            ('ME', 'Mechanical Engineering'))

    DESIG = (('Associate Professor', 'Associate Professor'),
             ('Assistant Professor', 'Assistant Professor'))

    CATEGORY = (('Permanent', 'Permanent'), ('Temporary', 'Temporary'))

    photo = models.FileField(upload_to=upload_location, null=True, blank=True)
    empid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    dept = models.CharField(max_length=70, choices=DEPT)
    dob = models.DateField()
    desig = models.CharField(max_length=20, choices=DESIG, default='Prof')
    permaddr = models.TextField(max_length=50)
    tempaddr = models.TextField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY, default='Temporary')
    email = models.EmailField()
    contact = models.IntegerField()
    status = models.CharField(max_length=10)
    datejoin = models.DateField()
    dateresig = models.DateField()
    accessLv = models.IntegerField()

    # after adding data to the database this func is called to redirect to the homepage
    #  def get_absolute_url(self):
    #     return reverse('student:index', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.empid) + '   ' + self.ename

    def get_absolute_url(self):
        return reverse('student:faculty_show', kwargs={'pk': self.pk})


class FacultySubject(models.Model):
    DEPT = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
            ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication Engineering'),
            ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
            ('ME', 'Mechanical Engineering'))

    SEMESTERS = (('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'),
                 ('8', 'S8'))

    YEARS = (tuple((x, x)) for x in range(2015, 2050))

    empid = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subcode = models.OneToOneField(Subject_Profile, on_delete=models.CASCADE)
    sem = models.CharField(max_length=2, choices=SEMESTERS, default='A')
    branch = models.CharField(max_length=50, choices=DEPT, default='A')
    section = models.CharField(max_length=1, choices=(('A', 'A'), ('B', 'B')), default='A')
    year = models.IntegerField(choices=YEARS)

    def __str__(self):
        return self.subcode.name

    def get_absolute_url(self):
        return reverse('student:index', kwargs={'pk': self.pk})


from django.contrib.auth.models import User
