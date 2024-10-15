from django.shortcuts import render


def show_course(request,name):
    return render(request,'course.html',{'name':name})

# Create your views here.
