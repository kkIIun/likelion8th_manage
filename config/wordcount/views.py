from django.shortcuts import render,redirect

# Create your views here.
def home(request) :
    return render(request, 'home.html') 

def wordcounter(request):
    dict = {}
    
    words = request.GET.get('input').split()
    for word in words :
        if word in dict :
            dict[word] += 1
        else :
            dict[word] = 1
        
    return render(request, 'home.html',{'dict':dict}) 