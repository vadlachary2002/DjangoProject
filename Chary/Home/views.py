from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
  # return HttpResponse("this is home page")
  context = {
    'name':"homeu"
  }
  return render(request,'index.html',context)

def services(request):
  context = {
    'name':"services"
  }
  return render(request,'services.html',context)

def login(request):
  context = {
    'name':"login"
  }
  return render(request,'login.html',context)

def about(request):
  context = {
    'name':"about"
  }
  return render(request,'about.html',context)

def contact(request):
  context = {
    'name':"contact"
  }
  return render(request,'contact.html',context)