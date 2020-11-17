# #
from django.shortcuts import render
from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse("HELLO WORLD")
def home(request):
     return render(request, "signin.html")
def add(request):
     val1 = int(request.GET["num1"])
     val2 = int(request.GET["num2"])
     res = val1 + val2
     return render(request, "result.html",{"result":res})
def login(request):
     return HttpResponse("LOGIN SUCCESSFULLY")


