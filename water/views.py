from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Client

# Create your views here.
def index(request):
    return render(request,'index.html')

def addrecord(request):
    name=request.POST['name']
    email=request.POST['email']
    contact=request.POST['phone']
    message=request.POST['message']
    client=Client(name=name,email=email,contact=contact,message=message)
    client.save()
    return HttpResponseRedirect(reverse('index'))