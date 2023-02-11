from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
   # return HttpResponse ("<h1 style='background:pink'> Hello! all this is my first Django apps </h1>")
    my_dict={"insert_me":"Iam coming from subfolder app1_home/reg.html file of app1_home"}
    return render(request, 'app1_home/reg.html', context=my_dict)







