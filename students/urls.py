from django.urls import path
from . import views


urlpatterns=[

    path('',views.main,name='main'),
    path('application/',views.student_application,name='application'),
    path('save/',views.save,name='save'),
    path('register/',views.student_registration,name='register'),
    path('save_details/',views.save_details,name='save_details'),
    path('login/',views.student_login_info,name='login'),
    path('validate/',views.validate,name='validate'),
    path('details/',views.students_details,name='details'),
    path('logout/',views.logout_page,name='logout'),
    path('staff/',views.staff_registration,name='staff'),
    path('save_staff/',views.save_staffdetails,name='save_staff'),
    path('staff_validate/',views.staff_validate,name='staff_validate'),
    path('staff_login/',views.staff_login,name='staff_login'),
    path('staff_details/',views.staff_detail,name='staff_detail'),
    path('staff_logout/',views.staff_logout,name='staff_logout'),
    path('total_staff/',views.total_staff,name='total_staff'),
    path('total_students/',views.total_students,name='total_students'),
    path('<str:dep_code>/details/',views.std_details,name='std_details'),
    path('<str:dep_code>/student_details/',views.student_details,name='student_details'),


]