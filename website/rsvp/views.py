from django.shortcuts import render

from rsvp.models import Guest

# Create your views here.
def index(request):
    guest = Guest.objects.all()
    return render(request, 'index.html', {
        'guest': guest
    })
    
def process(request):
    
    pass
    
def jp(request):
    
    return render(request, 'index_jp.html')
    
def nav(request):
    
    return render(request, 'nav.html')
    
def nav_jp(request):
    
    return render(request, 'nav_jp.html')
    
def guests(request):
    guests = Guest.objects.all()
    return render(request, 'guests.html', {'people' : guests})
    
def guests_jp(request):
    guests = Guest.objects.all()
    return render(request, 'guests_jp.html', {'people' : guests})