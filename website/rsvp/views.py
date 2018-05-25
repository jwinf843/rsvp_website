from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'index.html', {'people' : [1, 2, 3]})
    
def nav(request):
    
    return render(request, 'nav.html')
    
def guests(request):
    
    return render(request, 'guests.html', {'people' : [1, 2, 3]})