from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def ayah_view(request): 
  x = "ayah reda"
  y= "2221190098"
  return render (request, "ayah.html", 
                 context = {"name":x, "Id": y}) 

def myclasses_view (request) :
  return render (request , "classes.html") 
