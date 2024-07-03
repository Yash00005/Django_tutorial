from django.shortcuts import render , redirect

# Create your views here.

from django.http import HttpResponse
#For taking Ratings added by me
from .forms import ratingform
from django.urls import reverse

def index(request):
    return HttpResponse("Hello, Annant. You're at the polls index")


def rate_site(request):
    if request.method == 'POST':
        form = ratingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls')
        
    else:
        form = ratingform()

    return render(request, 'rate_site.html', {'form': form})

def my_view(request):
    url = reverse('polls') 
    return render(request, 'rate_site.html', {'url': url})

def polls_view(request):
    return render(request, 'polls/polls_template.html', context={})