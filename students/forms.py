from django.forms import ModelForm
from .models import Student, Staff,Register

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields=['student_name','student_email','student_phone','ssc_marks','inter_marks']
        #fields = "__all__"

# class RegisterForm(ModelForm):
#     class Meta:
#         model = Register
#         fields = "__all__"

class StaffForm(ModelForm):
    class Meta:
        model=Staff
        fields=['staff_name','staff_department','staff_email','staff_phone','qualification','experiance','photo']