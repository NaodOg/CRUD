from django.shortcuts import render, redirect
from registration.forms import studentform
from .models import student
# Create your views here.
def student_list(request):
    context ={'student_list':student.objects.all()}
    return render(request,'student_list.html', context)

def student_form(request, id=0):
    if request.method == "GET":
        if id==0:
           form = studentform
        else:
           Student= student.objects.get(pk=id)
           form= studentform(instance=Student)
        return render(request,'student_form.html', {'form': form})
    else:
        if id == 0:
           form= studentform(request.POST)
        else:
           Student= student.objects.get(pk=id)
           form= studentform(request.POST,instance=Student)
        if form.is_valid():
            form.save()
        return redirect('/list')


def student_delete(request,id):
    students = student.objects.get(pk=id)
    students.delete()
    return redirect('/list')


    return 