from django.shortcuts import render
from django.http import HttpResponse
import datetime

#Create your views here.
def index(request):
    today=datetime.datetime.now().date()
    return render(request,'index.html',{"today" : today})
    #return HttpResponse("Hello World!, you are at the todoApp index page.")

def about(request):
    return render(request,'about.html')
#    return HttpResponse("This is the about page of todoApp.")

def contact(request):
    name="Thanapon"
    surname="Yalan"
    email="thanaponyalan@gmail.com"
    return render(request,'contact.html',{"name" : name,"surname" : surname,"email" : email})