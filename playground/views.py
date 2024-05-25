from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view function takes request and returns a response

def say_hello(request):
    return render(request, "hello.html", {"name": "User!"})