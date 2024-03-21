from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def SiteBar(request):
    return render(request, 'Site/Bootstrap.html')