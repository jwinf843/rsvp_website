from django.shortcuts import render

from rsvp.models import Guest

# Create your views here.
def index(request):
    guest = Guest.objects.all()
    return render(request, 'index.html', {
        'guest': guest
    })
    
def nav(request):
    
    return render(request, 'nav.html')
    
def guests(request):
    
    return render(request, 'guests.html', {'people' : [1, 2, 3]})