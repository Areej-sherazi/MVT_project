from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import students
from .forms import *
# from templates import updateForm


# # Create your views here.

def list(request):
    student_list=students.objects.all()
    context={'student_list':student_list}
    return render(request,'myapp/index.html',context=context)

def student(request):
    if request.method=='POST':
        student = students()
        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.grade = request.POST.get("grade")

        if student.grade is not None:
            student.save()
            return redirect('/students/list/')
        else:
            # Handle the case where 'grade' is empty
            return HttpResponse("Grade cannot be empty")

    else:
        return render(request,'myapp/add_student.html')
    

def detail(request,id):
    student_single=students.objects.get(id=id)
    context={'student_single':student_single}
    return render(request,'myapp/detail.html',context=context)

def delete(request, id):
    student = students.objects.get(id=id)
    student.delete()
    context={'message': 'Student has been deleted'}
    return redirect('/students/list/')


def update(request,id):
    if request.method == 'POST':
        instance= students.objects.get(id=id)
        context={'instance':instance}
        return render(request, 'myapp/updateForm.html', context=context)
    else:
        return render(request, 'myapp/updateForm.html')







