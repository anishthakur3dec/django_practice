
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    context={
        "val1":"This is Anish",
        "val2":"This is kajal"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def project(request):
    return render(request,'project.html')