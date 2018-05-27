from django.shortcuts import render

from rsvp.models import Guest

# Create your views here.
def index(request):
    guest = Guest.objects.all()
    return render(request, 'index.html', {
        'guest': guest
    })
    
def jp(request):
    
    return render(request, 'index_jp.html')
    
def nav(request):
    
    return render(request, 'nav.html')
    
def nav_jp(request):
    
    return render(request, 'nav_jp.html')
    
def guests(request):
    
    return render(request, 'guests.html', {'people' : [1, 2, 3]})
    
def guests_jp(request):
    
    return render(request, 'guests_jp.html', {'people': [1, 2, 3]})