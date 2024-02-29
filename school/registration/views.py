from django.shortcuts import render
from registration.forms import studentform
# Create your views here.
def student_list(request):
    return render(request,'student_list.html')

def student_form(request):
    form= studentform()
    return render(request,'student_form.html',{'form':form})

def student_delete(request):
    return