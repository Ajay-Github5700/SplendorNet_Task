from django.shortcuts import render,redirect,HttpResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def hview(request):
    return render(request,'tapp1/home.html',{})

def addview(request):
    form=EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pro1/sv/')
    return render(request,'tapp1/add.html',{'form':form})

def showview(request):
    obj=Employee.objects.all()
    return render(request,'tapp1/show.html',{'obj':obj})

def updateview(request,u):
    obj1=Employee.objects.get(id=u)
    form=EmployeeForm(instance=obj1)
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=obj1)
        if form.is_valid():
            form.save()
            return redirect('/pro1/sv/')
    return render(request,'tapp1/add.html',{'form':form})


def deleteview(request,d):
    obj2=Employee.objects.get(id=d)
    obj2.delete()
    return redirect('/pro1/sv/')