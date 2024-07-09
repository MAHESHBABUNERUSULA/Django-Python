from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from StudentApp.models import Course, Student, City


# Create your views here.
def login_fun(request):
   if request.method=='POST':
    user_name=request.POST['txtuser']
    user_password=request.POST['txtpassword']
    u1= authenticate(username=user_name,password=user_password)
    if u1 is not None:
        if u1.is_superuser:
            request.session['Uname']=user_name
            login(request,u1)
            return redirect('home')
    else:
        return render(request,'index.html',{ 'msg':'username and password is incorrect'})
   else:
    return render(request,'index.html')


def reg_fun(request):
    if request.method == 'POST':  # this code will ececute when we click on submit button in registeration page
        u_name=request.POST['txtName']
        u_password=request.POST['txtPassword']
        u_email=request.POST['txtEmail']
        if User.objects.filter(username=u_name).exists():
               return render(request,'register.html',{'msg':'use Proper username'})
        else:
            u1 = User.objects.create_superuser(username=u_name,password=u_password,email=u_email)
            u1.save()
            return redirect('log')
    else:
        return render(request,'register.html')

@login_required
@never_cache
def home_fun(request):
    return render(request,'home.html',{'data':request.session['Uname']})

@login_required
@never_cache
def addcourse_fun(request):
    if request.method=='POST':
        c1=Course()
        c1.course_name=request.POST['txtCname']
        c1.course_duration=request.POST['txtCDuration']
        c1.course_fees=int(request.POST['txtCFee'])
        c1.save()
        return render(request,'addcourse.html',{'msg':'Successfully added'})
    else:
       return render(request,'addcourse.html')

@login_required
@never_cache
def displaycourse_fun(request):
    course_data= Course.objects.all()  # it will return list of objects in dictionary fromate
    return render(request,'displaycourse.html',{'data':course_data})

@login_required
@never_cache
def updatecourse_fun(request,cid):
    c1=Course.objects.get(id=cid)
    if request.method=='POST':
        c1.course_name=request.POST['txtCname']
        c1.course_duration=request.POST['txtCDuration']
        c1.course_fees=request.POST['txtCFee']
        c1.save()
        return redirect('display_course')
    else:
       return render(request,'updatecourse.html',{'data':c1})

@login_required
@never_cache
def deletecourse_fun(request,cid):
    c1=Course.objects.get(id=cid)
    c1.delete()  # delete the data which is inside the object
    return redirect('display_course')

@login_required
@never_cache
def addstudent_fun(request):
    if request.method == 'POST':
        s1=Student()
        s1.stud_name=request.POST['txtSname']
        s1.stud_phno=request.POST['txtSphno']
        s1.stud_email=request.POST['txtSemail']
        s1.stud_city=City.objects.get(city_name=request.POST['ddlcity'])
        s1.stud_course=Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.paid_fee=int(request.POST['txtPaidfee'])
        c1=Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.pending_fee=c1.course_fees - s1.paid_fee
        s1.save()
        return render(request,'addstudent.html',{'msg':'successfully added student details'})
    else:
        city=City.objects.all()
        course=Course.objects.all()
        return render(request,'addstudent.html',{'CityData': city,'CourseData': course})

@login_required
@never_cache
def displaystudent_fun(request):
    s1=Student.objects.all()
    return render(request,'displaystudent.html',{'student':s1})

@login_required
@never_cache
def updatestudent_fun(request,sid):
    s1=Student.objects.get(id=sid)
    if request.method == 'POST':

        s1.stud_name=request.POST['txtSname']
        s1.stud_phno=request.POST['txtSphno']
        s1.stud_email=request.POST['txtSemail']
        s1.stud_city=City.objects.get(city_name=request.POST['ddlcity'])
        s1.stud_course=Course.objects.get(course_name=request.POST['ddlcourse'])
        print(s1.paid_fee)
        s1.paid_fee = s1.paid_fee + int(request.POST['txtPaidfee'])
        c1=Course.objects.get(course_name=request.POST['ddlcourse'])
        if s1.pending_fee > 0:
              s1.pending_fee=c1.course_fees - s1.paid_fee
        else:
            s1.pending_fee = 0
        s1.save()
        return redirect('display_student')


    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request,'updatestudent.html',{'CityData': city,'CourseData': course,"studentdata":s1})

@login_required
@never_cache
def deletestudet_fun(request,sid):
    s1 = Student.objects.get(id=sid)
    s1.delete()  # delete the data which is inside the object
    return redirect('display_student')


def logout_fun(request):
    logout(request)
    return redirect('log')