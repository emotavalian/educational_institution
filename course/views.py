from django.shortcuts import render


def show_course(request,name):
    a=2
    b=3
    c=a*b
    return render(request,'course.html',{'name':name,'c':c})

# Create your views here.
