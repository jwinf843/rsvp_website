from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'index.html', {'people' : [1, 2, 3]})