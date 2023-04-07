from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def rent(request):
    return render(request,'rent.html')

