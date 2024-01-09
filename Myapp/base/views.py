
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    context={
        "val1":"This is Anish",
        "val2":"This is kajal"
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    return HttpResponse("this is contact")
def project(request):
    return HttpResponse("this is project page")