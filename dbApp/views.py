from django.shortcuts import render
from django.http import HttpResponse
from dbApp.models import Employee

# Create your views here.

def empDetails(request):
    emp_data = Employee.objects.all()
    emp_dict = {'emp_list':emp_data}
    return render(request,'employee.html',context = emp_dict)


