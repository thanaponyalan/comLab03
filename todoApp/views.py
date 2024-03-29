from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm

#Create your views here.
def index(request):
    if request.method=='POST':
        form=ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            allItems=List.objects.all
            return render(request,'index.html',{'all':allItems})
        
    else:
        allItems=List.objects.all
        return render(request,'index.html',{'all': allItems})

def about(request):
    return render(request,'about.html')

def contact(request):
    name="Thanapon"
    surname="Yalan"
    email="thanaponyalan@gmail.com"
    return render(request,'contact.html',{"name" : name,"surname" : surname,"email" : email})

def delete(request,itemID):
    item=List.objects.get(pk=itemID)
    item.delete()
    return redirect('home')

def changeCross(request,itemID):
    targetObj=List.objects.get(pk=itemID)
    targetObj.finished=not targetObj.finished
    targetObj.save()
    return redirect('home')