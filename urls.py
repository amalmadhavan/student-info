from django.urls import path
from django.contrib import admin

from django.conf.urls import url

from django.contrib.auth.views import LoginView
from . import views
from .models import Student
app_name='student'

urlpatterns= [
    #homepage

# url(r'^up/$',views.simple_upload,name='s'),

# url(r'^csv/$',views.upform,name='a'),

    # url(r'^regno-autocomplete/$',views.RegisterNumberAutoComplete.as_view(model=Student),name='regno-autocomplete'),
    # url(r'',views.LoginUserView.as_view(), name='login_new'),
    url(r'^a/$',views.t,name="test_pdf"),

    url(r'^email/$',views.email,name=""),

    url(r'^attendence_search/$',views.attendence_search,name="attendence_search"),

    # url(r'^sms/$',views.sms,name=""),

    url(r'^pdf/$',views.render_to_pdf,name='pdf_render'),

    url(r'^test/$',views.studentdetail_search,name='student_detail'),

    url(r'^public_form/$',views.search_form,name='public_marks_search'),

    url(r'^mark_pdf_form/$',views.pdf_form,name='pdf_form'),

    url(r'^report/(?P<regno>[0-9]+)/(?P<branch>[A-Z]+)/(?P<cursem>[0-8])/$',views.student_report,name='student_report'),

    url(r'^pa/',views.load_subject_code,name='subject_list'),

    url(r'^subname/',views.load_subject_name,name='subject_name'),

    url(r'^subname2/', views.load_subject_name2, name='subject_name2'),

    url(r'^login/$', LoginView.as_view(), name='login'),


    url(r'^addcsv/$', views.StudentCsv, name='student_addcsv'),

    url(r'^attendence_add/$',views.AttendenceCsv, name='attendence_csv'),

    url(r'^user_add/$',views.UserCsv,name='user_csv'),

    # url(r'^logtest/$',views.LoginUser.as_view(),name='testlog'),

    # url(r'^contact/$',views.ContactFormView1, name='submit'),

# url(r'^edits/$',views.Studentform_edit,name='s'),
    url(r'^mark_search/$',views.Marklistsearch,name='marklist_search'),

    url(r'^edit_marks/$',views.marklist_search,name="edit_marks"),

     url(r'^marks_search/$',views.searchmarks,name='ss'),

   url(r'^edits/(?P<regno>[0-9]+)/$',views.Studentform_edit,name='s'), # // okay working well

# url(r'^edits/(?P<branch>[A-Z]+)/$',views.Studentform_edit,name='s'),

# url(r'^edits/(?P<branch>[A-Z]+)/(?P<join>[0-9]+)/(?P<cursem>[0-8])/(?P<type>[A-Za-z]+)$',views.Studentform_edit,name='s'),

    url(r'^login_user/$',views.loguser,name='new_log'),

    url(r'^$', views.testing, name='index2'),

     url(r'^sss$', views.Indexview.as_view(), name='index'),

     url(r'^logout/$',views.logoutuser,name='logout'),



     url(r'^home/$',views.home,name='home'),

    #student/regno

    # for generic view DetailView url(r'^(?P<regno>[0-9]+)/$', views.Detailview.as_view(), name='detail'),
     # url(r'^(?P<regno>[0-9]+)/$', views.detail, name='detail'),

    #call form to add student url pattern
     # url(r'^add/$', views.Studentcreate.as_view(),name='student_add'),

    url(r'^add/$', views.StudentCreate,name='student_add'),

      url(r'^view/(?P<regno>[0-9]+)/$',views.detail,name='views'),

      #call form to update and view data the detail url
     # url(r'^edit/(?P<pk>[0-9]+)/$', views.Studentupdate.as_view(),name='detail'),

    url(r'^edit/(?P<pk>[0-9]+)/$', views.StudentUpdate,name='detail'),

      # url(r'edit/(?P<pk>[0-9]+)(?P<branch>[a-z]+)/',views.Studentupdate.as_view(),name='details')

   # url(r'^edits/(?P<pk>[0-9]+)/delete/$', views.Studentdelete.as_view(), name='delete'),

       url(r'^delete/(?P<pk>[0-9]+)/$', views.Studentdelete.as_view(), name='delete'),

     url(r'^search_form/$',views.Studentsearch,name='searchform'),

       url(r'^search/$',views.searchs,name='search'),

    #added this for making detailview generic view

     # url(r'^view/(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='view'),

     #register user to login
     url(r'^register/$',views.UserFormView.as_view(),name='register'),

    url(r'^register1/$',views.Studentform,name='aaaa'),


    url(r'^test/$',views.testing,name='test'),

    url(r'^stu_search/$',views.student_search,name='student_search'),




    # for faculty
    url(r'^fac_search/$',views.faculty_search,name='faculty_search'),

    url(r'^faculty/$',views.Facultyview.as_view(),name='faculty_show'),


    url(r'^faculty_details/(?P<empid_id>[0-9]+)/$',views.FacultyDetail,name='faculty_details'),


    url(r'^faculty_add/$',views.FacultyCreate,name='faculty_add'),

    #for update view pk should be the name passed as arguments
    url(r'^faculty_edit/(?P<empid_id>[0-9]+)/$', views.Facultyupdate, name='faculty_edit'),

    url(r'^faculty_delete/(?P<pk>[0-9]+)/$', views.Facultydelete.as_view(), name='faculty_delete'),

    url(r'^facultysubject_search/$', views.facultysubject_search, name='facultysubject_search'),




  #subject
    url(r'^list_subjects/$',views.SubjectsList,name='subjects_list'),

    url(r'^faculty_addsubmap/$',views.FacultySubMapCreate,name='faculty_addsubmap'),

    # url(r'^faculty_editsubmap/(?P<id>[0-9]+)/$',views.FacultySubMapEdit.as_view(),name='faculty_editsubmap'),



  #marklist
    # url(r'^marklist_add/$'views.MarklistCreate.as_view(),name='marklist_add'),


url(r'^marklist_add/$',views.MarklistCreate,name='marklist_add'),

    url(r'^marklist_edit/(?P<regno>[0-9]+)/(?P<branch>[A-Z]+)/(?P<cursem>[0-9]+)/(?P<section>[A-B]+)/(?P<type>[A-Za-z]+)$', views.MarklistUpdate, name='marklist_edit'),

    url(r'^marklist_csv',views.MarklistCsv,name="marklist_csv"),

    url(r'^attendence_edit/(?P<regno>[0-9]+)/(?P<cursem>[0-9]+)/(?P<section>[A-B]+)/(?P<id>[0-9]+)',
        views.AttendenceUpdate, name='attendence_edit'),

#
url(r'^attendence_calc/(?P<regno>[0-9]+)/(?P<section>[A-B]+)/(?P<cursem>[0-9]+)/(?P<id>[0-9]+)',
        views.attendence_calc, name='attendence_calc'),

    #subject_profile

    # url(r'^subject_add/$',views.Subject_ProfileCreate.as_view(),name='subject_add'),

    # url(r'^subject_edit/(?P<pk>[A-Z]+[_]+[0-9]+)/$', views.Subject_ProfileEdit.as_view(), name='subject_edit'),

  #subject_profile

    url(r'^subject_add/$',views.Subject_ProfileCreate,name='subject_add'),

    url(r'^subject_edit/(?P<pk>[A-Z]+[_]+[0-9]+)/$', views.Subject_ProfileEdit.as_view(), name='subject_edit'),


    #for syllabus
    # url(r'^syllabus_add/$',views.SyllabusCreate.as_view(),name='syllabus_add'),

    url(r'^syllabus_add/$',views.SyllabusCreate,name='syllabus_add'),

    url(r'^syllabus_edit/(?P<pk>[0-9]+)/$', views.SyllabusEdit, name='syllabus_edit'),

    url(r'^syllabus_search/$',views.syllabus_search,name='syllabus_search'),


     url(r'^subjectprofile_view/(?P<id>[0-9]+)/$',views.subjectprofileview,name='subjectprofile_list'),


     url(r'^subjectprofile_edit/(?P<id>[0-9]+)$',views.subjectprofileedit,name='subjectprofile_edit'),

    url(r'^regnoroll/$',views.RollnoRegnoMapAdd,name='regno_map'),


    url(r'^attendence_pdf_search/$',views.attendence_pdf,name='attendence_pdf_search'),

    url(r'^attendence_list/$',views.attendence_list_pdf,name='attendence_list'),

    url(r'^attendence_search/$',views.attendence_search,name='attendence_search'),

    # url(r'^attendence_edit/(?P<year>[0-9]+)/(?P<branch>[A-Z]+)/(?P<cursem>[0-9]+)/(?P<section>[A-B]+)',views.attendenceedit,name='attendence_edit'),



    # user.year/user.branch/user.cursem/user.section

    #
    # url(r'^regnoroll/(?P<pk>[0-9]+)/$', views.RollnoRegnoMapEdit.as_view(), ),
    #
    # url(r'^facultymap/$',views.StudentFacultyLabMapAdd,),
    #
    # url(r'^facultymap/(?P<pk>[0-9]+)/$',views.StudentFacultyLabMapEdit.as_view(),),
    # #
    # url(r'student_login/',views.student_login),



]




