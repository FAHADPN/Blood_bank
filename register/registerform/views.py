from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def form(request):
    name = request.GET["name"]
    email = request.GET["Email"]
    cnumber = request.GET["cnumber"]

    return render(request, 'results.html',{'name':name,'email':email,'cnumber':cnumber})