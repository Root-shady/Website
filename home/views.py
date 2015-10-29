from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
def home(request):
    context_dict = {
            'user':'shady'
            }
    return render(request, 'home/home.html', context_dict)
def about(request):
    context_dict = {
            'user':'shady'
            }
    return render(request, 'home/about.html', context_dict)
