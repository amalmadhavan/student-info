from django.db import models
from django.urls import reverse
import datetime
from django.utils.timezone import now
from django.core.mail import send_mail

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, UnicodeUsernameValidator
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
            Create and save a user with the given username, email, and password.
            """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    DEPT = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
            ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
            ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
            ('ME', 'Mechanical Engineering'))

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    email = models.EmailField(('email address'), blank=True)
    dept = models.CharField(max_length=70, choices=DEPT)
    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(('date joined'), default=now())

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        # abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)



def upload_location(instance, filename):
    return "student/%s/%s" % (instance.regno, filename)


class Student(models.Model):  
    SECTION = (('A', 'A'), ('B', 'B'))

    BRANCHES = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
                ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
                ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
                ('ME', 'Mechanical Engineering'))

    SEMESTERS = (('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'),
                 ('8', 'S8'))

    STATUS = (('Active', 'Currently Studying'), ('Pass out', 'Course Completed'),
              ('Drop out', 'Drop out '))

    BLOODGROUPS = (('A+ve', 'A+ve'), ('A-ve', 'A-ve'), ('B+ve', 'B+ve'),
                   ('B-ve', 'B-ve'), ('AB+ve', 'AB+ve'), ('AB-ve', 'AB-ve'),
                   ('O+ve', 'O+ve'), ('O-ve', 'O-ve'),)

    GENDER = (('M', 'Male'), ('F', 'Female'))

    YEARS = []
    limit = datetime.datetime.today().year + 10
    for x in range(2015, limit):
        YEARS.append((x, x))

    # YEARS = (tuple((x, x)) for x in range(2015, 2025))

    ADM = (('Regular', 'Regular'), ('Lateral Entry', 'Lateral Entry'))

    photo = models.FileField(upload_to=upload_location, null=True, blank=True)
    regno = models.IntegerField(primary_key=True, verbose_name='Register Number')
    name = models.CharField(max_length=30, verbose_name='Name')
    branch = models.CharField(max_length=15, choices=BRANCHES)
    cursem = models.CharField(max_length=2, choices=SEMESTERS, verbose_name='Semester')
    join = models.IntegerField(choices=YEARS, verbose_name='Year Of Join')
    section = models.CharField(max_length=1, choices=SECTION)
    status = models.CharField(max_length=20, choices=STATUS, default='Active')
    admtype = models.CharField(max_length=20, choices=ADM, default='Regular')
    gender = models.CharField(max_length=6, choices=GENDER, default='M')

    admissionno = models.IntegerField(verbose_name='Admission Number', default='0')
    permanentaddress = models.CharField(max_length=150, verbose_name='Permanent Address', null=True, blank=True)
    temporaryaddress = models.CharField(max_length=150, verbose_name='Temporary Address', null=True, blank=True)
    dateofbirth = models.DateField(default='2000-01-01')

    category = models.CharField(max_length=20, default='General')
    emailid = models.CharField(max_length=80, verbose_name=u'Email Id', null=True, blank=True)
    personwithdisabilities = models.CharField(max_length=40, verbose_name='Person with Disabilities', null=True,
                                              blank=True)
    catrank = models.IntegerField(verbose_name='CAT Rank', default='0')
    religion = models.CharField(max_length=15, null=True, blank=True)
    bloodgroup = models.CharField(max_length=6, verbose_name='Blood Group', choices=BLOODGROUPS)

    parentorguardianname = models.CharField(max_length=50, verbose_name='Parent/Guardians Name', null=True, blank=True)
    parentorguardianoccupation = models.CharField(max_length=15, verbose_name='Parent/Guardians Occupation', null=True,
                                                  blank=True)
    parentorguardiancontactno = models.CharField(max_length=15, verbose_name='Parent/Guardians Contact No', null=True,
                                                 blank=True)
    parentorguardianemailid = models.CharField(max_length=50, verbose_name='Parent/Guardians Email Id', null=True,
                                               blank=True)
    miniproject = models.CharField(max_length=100, verbose_name='Mini Project', null=True, blank=True)
    miniprojectguide = models.CharField(max_length=25, verbose_name='Mini Project Guide', null=True, blank=True)
    mainproject = models.CharField(max_length=100, verbose_name='Main Project', null=True, blank=True)
    mainprojectguide = models.CharField(max_length=25, verbose_name='Main Project Guide', null=True, blank=True)
    behaviour = models.CharField(max_length=100, default='Good')
    studentcontactno = models.CharField(max_length=15, verbose_name='Students Contact No', null=True, blank=True)
    studentemailid = models.CharField(max_length=50, verbose_name='Students Email Id', null=True, blank=True)

    tenboard = models.CharField(max_length=20, verbose_name='10th Board', null=True, blank=True)
    tenregisterno = models.IntegerField(verbose_name='10th Register No', null=True, blank=True)
    tenmarks = models.IntegerField(verbose_name='10th Marks', null=True, blank=True)
    tenpercentage = models.IntegerField(verbose_name='10th Percentage', null=True, blank=True)
    tenyear = models.IntegerField(default='0')

    qualifyingboard = models.CharField(max_length=20, verbose_name='Qualifying Board', null=True, blank=True)
    qualifyingregisterno = models.IntegerField(verbose_name='Qualifying Register No', null=True, blank=True)
    qualifyingmarks = models.IntegerField(verbose_name='Qualifying Marks', null=True, blank=True)
    qualifyingpercentage = models.IntegerField(verbose_name='Qualifying Percentage', null=True, blank=True)
    qualifyingyear = models.IntegerField(verbose_name='Qualifying Year', null=True, blank=True)
    specialreservation = models.CharField(max_length=30, verbose_name='Special Reservation', null=True, blank=True)

    # after adding data to the database this func is called to redirect to the homepage
    def get_absolute_url(self):
        return reverse('student:index', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.regno)

    class Meta:
        ordering = ('regno',)


class Syllabus(models.Model):
    DEPT = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
            ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication Engineering'),
            ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
            ('ME', 'Mechanical Engineering'))

    YEARS = []
    limit = datetime.datetime.today().year + 10
    for x in range(2015, limit):
        YEARS.append((x, x))

    year = models.PositiveIntegerField(choices=YEARS)
    dept = models.CharField(max_length=60, choices=DEPT, verbose_name='Department')

    theory_max_internal = models.PositiveIntegerField()
    theory_max_external = models.PositiveIntegerField()

    lab_max_internal = models.PositiveIntegerField()
    lab_max_external = models.PositiveIntegerField()

    def __str__(self):
        return str(self.year)

    class Meta:
        ordering = ('year',)


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
        return self.code

    class Meta:
        ordering = ('code',)


class Marklist(models.Model):
    SECTION = (('A', 'A'), ('B', 'B'))

    BRANHCES = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
                ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
                ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
                ('ME', 'Mechanical Engineering'))

    SEMESTERS = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                 ('8', '8'))

    EXAMS = (('Internal', 'Internal'), ('External', 'External'))

    CHANCES = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))

    # YEARS = (tuple((x, x)) for x in range(2015, 2025))
    YEARS = []
    limit = datetime.datetime.today().year + 10
    for x in range(2015, limit):
        YEARS.append((x, x))

    # regno = models.ForeignKey(Student, on_delete=models.CASCADE, default='0')
    regno = models.ForeignKey(Student, on_delete=models.CASCADE)
    branch = models.CharField(max_length=70, choices=BRANHCES)
    cursem = models.CharField(max_length=2, choices=SEMESTERS)
    section = models.CharField(max_length=1, choices=SECTION)
    type = models.CharField(max_length=9, choices=EXAMS, default='Internal')
    join = models.IntegerField(choices=YEARS, default='0')
    chance = models.IntegerField(default='0')

    subcode1 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Subcode1')
    # subcode1 = models.CharField(max_length=10, default='0')
    # sub1 = models.ForeignKey(Subject_Profile,on_delete=models.CASCADE,related_name='Sub1')
    # sub1 = models.CharField(max_length=60, default='0')

    mark1 = models.SmallIntegerField(default='0')

    subcode2 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Subcode2')

    # subcode2 = models.CharField(max_length=10, default='0')
    # sub2 = models.CharField(max_length=60, default='0')
    # sub2 = models.ForeignKey(Subject_Profile,on_delete=models.CASCADE,related_name='Sub2')

    mark2 = models.SmallIntegerField(default='0')

    subcode3 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Subcode3')
    # sub3 = models.CharField(max_length=60, default='0')
    # sub3 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Sub3')
    mark3 = models.SmallIntegerField(default='0')

    subcode4 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Subcode4')
    # sub4 = models.CharField(max_length=60, default='0')
    # sub4 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Sub4')
    mark4 = models.SmallIntegerField(default='0')

    subcode5 = models.CharField(max_length=15, default='0',blank=True,null=True)
    # sub5 = models.CharField(max_length=70, default='0')
    # sub5 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Sub5')
    mark5 = models.SmallIntegerField(default='0')

    subcode6 = models.CharField(max_length=15, default='0',blank=True,null=True)
    # sub6 = models.CharField(max_length=70, default='0')
    # sub6 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Sub6')
    mark6 = models.SmallIntegerField(default='0',blank=True,null=True)

    subcodel1 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Subcodel1')
    # subl1 = models.CharField(max_length=60, default='0')
    # subl1 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Subl1')

    markl1 = models.SmallIntegerField(default='0')

    subcodel2 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Subcodel2')

    # subl2 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Subl2')
    # subl2 = models.CharField(max_length=60, default='0')
    markl2 = models.SmallIntegerField(default='0')

    subcodel3 = models.CharField(max_length=15, default='0',blank=True,null=True)
    # subl3 = models.CharField(max_length=60,default='')
    # subl3 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Subl3')
    markl3 = models.SmallIntegerField(default='0',blank=True,null=True)

    subcodel4 = models.CharField(max_length=15, default='0',blank=True,null=True)
    # subl4 = models.CharField(max_length=60,default='')
    # subl4 = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, related_name='Subl4')
    markl4 = models.SmallIntegerField(blank=True, default='0')

    def __str__(self):
        return str(self.regno.regno) +' S' + str(self.cursem)

    class Meta:
        ordering = ('regno',)


def upload_location2(instance, filename):
    return "faculty/%s/%s" % (instance.empid, filename)


class Faculty(models.Model):
    DEPT = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
            ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
            ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
            ('ME', 'Mechanical Engineering'))

    DESIG = (('Associate Professor', 'Associate Professor'),
             ('Assistant Professor', 'Assistant Professor'))

    CATEGORY = (('Permanent', 'Permanent'), ('Temporary', 'Temporary'))

    photo = models.FileField(upload_to=upload_location2, null=True, blank=True)
    empid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    dept = models.CharField(max_length=70, choices=DEPT, verbose_name='Department')
    dob = models.DateField(help_text='dd-mm-yyyy')
    desig = models.CharField(max_length=20, choices=DESIG, default='Prof', verbose_name='Designation')
    permaddr = models.TextField(max_length=50)
    tempaddr = models.TextField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY, default='Temporary')
    email = models.EmailField()
    contact = models.CharField(max_length=13)
    status = models.CharField(max_length=10)
    datejoin = models.DateField(null=True,blank=True)
    dateresig = models.DateField(null=True,blank=True)

    # accessLv = models.IntegerField()

    # after adding data to the database this func is called to redirect to the homepage
    #  def get_absolute_url(self):
    #     return reverse('student:index', kwargs={'pk': self.pk})

    def __str__(self):
        # return str(self.regno.regno) + ' ' + str(self.regno.name)
        return str(self.empid) + ' '+ str(self.ename)

    def get_absolute_url(self):
        return reverse('student:faculty_show', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('empid',)


class FacultySubject(models.Model):
    DEPT = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
            ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication Engineering'),
            ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
            ('ME', 'Mechanical Engineering'))

    SEMESTERS = (('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'),
                 ('8', 'S8'))

    YEARS = []
    limit = datetime.datetime.today().year + 10
    for x in range(2015, limit):
        YEARS.append((x, x))

    SECTION = (('A', 'A'), ('B', 'B'))

    empid = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subcode = models.OneToOneField(Subject_Profile, on_delete=models.CASCADE, verbose_name='Subject Code')
    sem = models.CharField(max_length=2, choices=SEMESTERS, default='0', verbose_name='Semester')
    branch = models.CharField(max_length=50, choices=DEPT, default='A', verbose_name='Branch')
    section = models.CharField(max_length=1, choices=SECTION, default='A', verbose_name='Section')
    year = models.IntegerField(choices=YEARS, verbose_name='Year Of Join')

    def __str__(self):
        return self.subcode.name

    def get_absolute_url(self):
        return reverse('student:index', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('empid',)


class RollnoRegnoMap(models.Model):
    SECTION = (('A', 'A'), ('B', 'B'))

    BRANCHES = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
                ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication Engineering'),
                ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
                ('ME', 'Mechanical Engineering'))

    ATTEND = (('N', 'Null'), ('P', 'Present'), ('A', 'Absent'),)

    SEMESTERS = (('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'),
                 ('8', 'S8'))

    YEARS = []
    limit = datetime.datetime.today().year + 10
    for x in range(2015, limit):
        YEARS.append((x, x))

    # id = models.AutoField()
    regno = models.IntegerField()
    rollno = models.IntegerField()
    name = models.CharField(max_length=50, default='')
    section = models.CharField(max_length=1, choices=SECTION)
    year = models.IntegerField(choices=YEARS)
    branch = models.CharField(max_length=50, choices=BRANCHES)
    cursem = models.CharField(max_length=4, choices=SEMESTERS, default='0', verbose_name='Semester')
    facultyid = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name='Facuty Id')
    subjectcode = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE, verbose_name='Subject Code')
    firsthr = models.CharField(choices=ATTEND, max_length=10, default='Null')
    secondhr = models.CharField(choices=ATTEND, max_length=10, default='Null')
    thirdhr = models.CharField(choices=ATTEND, max_length=10, default='Null')
    fourthhr = models.CharField(choices=ATTEND, max_length=10, default='Null')
    fifthhr = models.CharField(choices=ATTEND, max_length=10, default='Null')
    sixthhr = models.CharField(choices=ATTEND, max_length=10, default='Null')
    ptotal = models.IntegerField(default='-1')
    atotal = models.IntegerField(default='-1')
    ftotal = models.IntegerField(default='-1')
    time = models.DateTimeField(default=now())

    def __str__(self):
        return str(self.rollno) + "_" + str(self.regno)

    def get_absolute_url(self):
        return reverse('student:home', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('id',)
        get_latest_by = 'time'

# class StudentFacultyLabMap(models.Model):
#     BRANCHES = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
#                 ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication Engineering'),
#                 ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
#                 ('ME', 'Mechanical Engineering'))
#
#     SEMESTERS = (('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'),
#                  ('8', 'S8'))
#
#     regno = models.ManyToManyField(RollnoRegnoMap)
#     subcode = models.ForeignKey(Subject_Profile, on_delete=models.CASCADE)
#     facultyid = models.ForeignKey(Faculty, on_delete=models.CASCADE)
#     # present=models.BooleanField()
#     branch = models.CharField(max_length=50, choices=BRANCHES)
#     cursem = models.CharField(max_length=2, choices=SEMESTERS)
#
#     def __str__(self):
#         return str(self.regno)
#
#     def get_absolute_url(self):
#         return reverse('student:index', kwargs={'pk': self.pk})
