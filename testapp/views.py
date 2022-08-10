from django.shortcuts import render
from django.http import HttpResponse

def sout(request,you):
    return HttpResponse("hi "+ str(you))
def html(request):
    return render(request,'index.html')