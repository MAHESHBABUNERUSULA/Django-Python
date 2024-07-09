from django.urls import path

from StudentApp import views

urlpatterns=[
    path('',views.login_fun,name='log'), # it will redirect to index
    path('reg',views.reg_fun,name='reg'), # it will redirect to register.html page
    path('home',views.home_fun,name='home'),  # it will redirect to home.html page
    path('add_course',views.addcourse_fun,name='add_course'), # it will redirect to addcourse,html page
                                                              # inserting course data into course table
    path('display_course',views.displaycourse_fun,name='display_course'),  # it will collect data frome course table and it will send to displaycourse.html
    path('update_course/<int:cid>',views.updatecourse_fun,name='update_course'),
    path('delete_course/<int:cid>',views.deletecourse_fun,name='delete_course'),
    path('add_student',views.addstudent_fun,name='add_student'),  # it will display addstudent.html file and store into student table
    path('display_student',views.displaystudent_fun,name='display_student'),
    path('update_student/<int:sid>',views.updatestudent_fun,name='update_student'),
    path('delete_student<int:sid>',views.deletestudet_fun,name='delete_student'),
    path('logout',views.logout_fun,name='logout')
]