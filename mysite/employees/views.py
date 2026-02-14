from django.shortcuts import render

from .models import Employee

# Create your views here.
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        print(employee)
    except Employee.DoesNotExist:
        return render(request, 'employee_not_found.html', status=404)