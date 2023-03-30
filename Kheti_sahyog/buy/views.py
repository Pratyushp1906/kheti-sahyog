from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def buyrent(request):
    return render(request,'buy.html')

def sellrent(request):
    return render(request,'sell.html')