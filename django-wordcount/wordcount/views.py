from django.shortcuts import render,redirect
from .models import Pictures
from django.core.paginator import Paginator
# Create your views here.
def home(request) :
    blogs = Pictures.objects.all()
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html',{'posts':posts}) 

def wordcounter(request):
    dict = {}
    
    words = request.GET.get('input').split()
    for word in words :
        if word in dict :
            dict[word] += 1
        else :
            dict[word] = 1
        
    return render(request, 'home.html',{'dict':dict}) 