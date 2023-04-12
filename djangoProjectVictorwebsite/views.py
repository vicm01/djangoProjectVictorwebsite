from django.shortcuts import render

def indexpage(request):
    return render(request, "index.html")

def aboutpage(request):
    return render(request, "about.html")

def servicepage(request):
    return render(request, "service.html")