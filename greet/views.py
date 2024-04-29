from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

def greet(request, name):
    context = {
        "name" : name.capitalize()
    }
    return render(request,"greet/index.html", context)


    # return render(request,"greet/index.html",{
    #     "name" : name.capitalize()
    # })
    #return render (request, "hello/index.html")


def hello(request):
    return HttpResponse("<h4>This is heading 4</h4>")