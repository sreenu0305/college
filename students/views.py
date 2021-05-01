from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from students.models import Student, Register, Staff,Department
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
import pdb
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .forms import StaffForm


def main(request):
    return render(request, 'students/main.html')


def student_application(request):
    form = StudentForm()
    return render(request, 'students/application.html',{"form":form})


def save(request):
    if request.method=='POST':
        form_obj=StudentForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return render(request,'students/application.html',{'form':StudentForm(),'error':form_obj.errors})
    #Student.objects.create(student_name=request.POST['name'], student_email=request.POST['email'],
    #                       student_phone=request.POST['phone'], ssc_marks=request.POST['ssc_marks'],
    #                         request.POST[inter_marks='inter_marks'])

    return HttpResponseRedirect('/students/')


def student_registration(request):
    # form = RegisterForm()
    deps = Department.objects.all()
    return render(request, 'students/register.html', {"deps": deps})


def save_details(request):
    if Student.objects.filter(student_email=request.POST['email'], is_verified=True).exists():
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        student = Student.objects.get(student_email=request.POST["email"])
        dep = Department.objects.get(code=request.POST['code'])
        Register.objects.create( image=request.FILES['image'], department=dep, user=user,Student=student)
        return HttpResponseRedirect('/students/')
    else:
        return render(request, 'students/application.html', {'error': 'you are not a valid user'})


def student_login_info(request):
    return render(request, 'students/login.html')


def validate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:

        login(request, user)
        if Register.objects.filter(user=user).exists():
            return HttpResponseRedirect('/students/details/')
        else:
            return render(request, 'students/login.html', {'error': 'Invalid username or password'})

    else:
        return render(request, 'students/login.html', {'error': 'Invalid username or password'})


@login_required(login_url="/students/login/")
def students_details(request):
    #pdb.set_trace()
    user = request.user
    return render(request, 'students/details.html', {'user':user})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/students/login/')


def staff_registration(request):
    form=StaffForm()
    return render(request, 'students/staff.html',{'form':form})


def save_staffdetails(request):
    form_obj=StaffForm(request.POST,request.FILES)
    if form_obj.is_valid():
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        staff = form_obj.save(commit=False)
        staff.user = user
        staff.save()

        return render(request,'students/staff.html',{'form':StaffForm,'error':form_obj.errors})

    # Staff.objects.create(staff_name=request.POST['name'], staff_email=request.POST['email'],
    #                      staff_phone=request.POST['phone'], qualification=request.POST['qualification'],
    #                      staff_department=request.POST['department'],
    #                      experiance=request.POST['experiance'], photo=request.FILES['photo'], user=user)


    return HttpResponseRedirect('/students/')





def staff_validate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        if Staff.objects.filter(user=user).exists():
            return HttpResponseRedirect('/students/staff_details/')
        else:
            return render(request,'students/staff.html', {'error': 'you are not a valid user'})
    else:
        return render(request, 'students/staff.html', {'error': 'you are not a valid user'})


def staff_login(request):
    return render(request, 'students/staff_login.html')


@login_required(login_url="/students/staff_login/")
def staff_detail(request):
    # pdb.set_trace()
    user = request.user
    return render(request, 'students/staff_details.html', {'user': user})


def staff_logout(request):
    logout(request)
    return HttpResponseRedirect('/students/staff_login/')


@login_required(login_url="/students/staff_login/")
def total_staff(request):
    # pdb.set_trace()
    staff = Staff.objects.all()
    return render(request, 'students/totalstaff.html', {'staff': staff})


@login_required(login_url="/students/staff_login/")
def total_students(request):
    # pdb.set_trace()
    deps = Department.objects.all()
    return render(request, 'students/total_students.html', {"deps": deps})

@login_required(login_url="/students/staff_login/")
def std_details(request, dep_code):
    student = Register.objects.filter(department__code=dep_code)
    return render(request, 'students/mechstudents.html', {'student': student})

@login_required(login_url="/students/login/")
def student_details(request,dep_code):
    student=Register.objects.filter(department__code=dep_code)
    return render(request,'students/students.html',{'student':student})