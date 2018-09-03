from django.shortcuts import render
from django.http import HttpResponse
from rsvp.models import Guest
from django.conf import settings
import os

# Create your views here.
def index(request):
    guest = Guest.objects.all()
    
    if request.method == 'GET':
        return render(request, 'index.html', {
        'guest': guest
    })
    
    #Post Request Data
    guest = Guest(
        name=request.POST['name'], 
        email=request.POST['email'], 
        rsvp=request.POST['rsvp'],
        additions=request.POST['additions'],
        message=request.POST['message'],
        )
    
    return render(request, 'rsvp.html')
    

def process(request):
    required_fields = ['rsvp', 'name', 'email']
    print(request.POST)
    for field in required_fields:
        if field not in request.POST:
            return HttpResponse('Error missing field.')

    #Post Request Data
    rsvp_val=True
    if request.POST['rsvp'] == 'True':
            rsvp_val=True
    elif request.POST['rsvp'] == 'False':
            rsvp_val=False
    
    guest = Guest(
        name=request.POST['name'], 
        email=request.POST['email'], 
        rsvp=rsvp_val,
        additions=request.POST['additions'],
        message=request.POST['message'],
        )
        
    guest.save()
    print("ID %s:" % guest.id)
    return render(request, 'process.html')
    
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
    
def album(request):
    photo_urls = []
    photo_file_path = os.path.join(settings.PROJECT_DIR, 'photos.txt')
    with open(photo_file_path) as fp:
        for line in fp:
            line = line.strip()  # Remove whitespace
            if line:
                photo_pair = (line + 'm.jpg', line + '.jpg')
                photo_urls.append(photo_pair)

    return render(request, 'album.html', {
    'photo_urls': photo_urls
    })
    
def album_jp(request):
    
    return render(request, 'album_jp.html')