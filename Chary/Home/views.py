from django.shortcuts import render,HttpResponse
from Home.models import Contact
from datetime import datetime
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
  if request.method=="POST":
    username =  request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    con = Contact(username=username, email=email,password=password)
    con.save()
  return render(request,'contact.html',{
      'name':"about"
    })