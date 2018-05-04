from django.urls import path
from django.contrib import admin

from django.conf.urls import url

from django.contrib.auth.views import LoginView
from . import views

app_name='student'
urlpatterns= [
    #homepage

     # url(r'^logtest/$',views.LoginUser.as_view(),name='testlog'),
    url(r'^sss$', views.testing, name='index2'),

     url(r'^$', views.Indexview.as_view(), name='index'),

   url(r'^login/$',LoginView.as_view(),name='login'),

     url(r'^home/$',views.home,name='home'),

    #student/regno

    # for generic view DetailView url(r'^(?P<regno>[0-9]+)/$', views.Detailview.as_view(), name='detail'),
     # url(r'^(?P<regno>[0-9]+)/$', views.detail, name='detail'),

    #call form to add student url pattern
     url(r'^add/$', views.Studentcreate.as_view(),name='student_add'),

   url(r'^view/(?P<regno>[0-9]+)/$',views.detail,name='views'),

      #call form to update and view data the detail url
    url(r'^edit/(?P<pk>[0-9]+)/$', views.Studentupdate.as_view(),name='detail'),

      # url(r'edit/(?P<pk>[0-9]+)(?P<branch>[a-z]+)/',views.Studentupdate.as_view(),name='details')

   # url(r'^edits/(?P<pk>[0-9]+)/delete/$', views.Studentdelete.as_view(), name='delete'),

       url(r'^delete/(?P<pk>[0-9]+)/$', views.Studentdelete.as_view(), name='delete'),

     url(r'^search_form/$',views.Studentsearch,name='searchform'),

       url(r'^search/$',views.searchs,name='search'),

    #added this for making detailview generic view

     # url(r'^view/(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='view'),

     #register user to login
     url(r'^register/$',views.UserFormView.as_view(),name='register'),


    url(r'^test/$',views.testing,name='test'),

    url(r'^stu_search/$',views.student_search,name='student_search'),




    # for faculty
    url(r'^fac_search/$',views.faculty_search,name='faculty_search'),

    url(r'^faculty/$',views.Facultyview.as_view(),name='faculty_show'),

   url(r'^faculty_details/(?P<empid>[0-9]+)/$',views.FacultyDetail,name='faculty_details'),


    url(r'^faculty_add/$',views.FacultyCreate.as_view(),name='faculty_add'),

    #for update view pk should be the name passed as arguments
    url(r'^faculty_edit/(?P<pk>[0-9]+)/$', views.Facultyupdate.as_view(), name='faculty_edit'),

    url(r'^faculty_delete/(?P<pk>[0-9]+)/$', views.Facultydelete.as_view(), name='faculty_delete'),






  #subject
    url(r'^list_subjects/$',views.SubjectsList,name='subjects_list'),

    url(r'^faculty_addsubmap/$',views.FacultySubMapCreate.as_view(),name='faculty_addsubmap'),

    url(r'^faculty_editsubmap/(?P<id>[0-9]+)/$',views.FacultySubMapEdit.as_view(),name='faculty_editsubmap'),



  #marklist
    url(r'^marklist_add/$',views.MarklistCreate.as_view(),name='marklist_add'),

    url(r'^marklist_edit/(?P<pk>[0-9]+)/$', views.MarklistUpdate.as_view(), name='marklist_edit'),



  #subject_profile

    url(r'^subject_add/$',views.Subject_ProfileCreate.as_view(),name='subject_add'),

    # url(r'^subject_edit/(?P<pk>[A-Z]+[_]+[0-9]+)/$', views.Subject_ProfileEdit.as_view(), name='subject_edit'),

  #subject_profile

    url(r'^subject_add/$',views.Subject_ProfileCreate.as_view(),name='subject_add'),

    # url(r'^subject_edit/(?P<pk>[A-Z]+[_]+[0-9]+)/$', views.Subject_ProfileEdit.as_view(), name='subject_edit'),


    #for syllabus
    url(r'^syllabus_add/$',views.SyllabusCreate.as_view(),name='syllabus_add'),


url(r'^syllabus_edit/(?P<pk>[0-9]+)/$', views.SyllabusEdit.as_view(), name='syllabus_edit'),



]




