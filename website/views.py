from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VideoForm
import sys
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.
def search(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        videotitle=request.POST['videoname']

        url = "https://en.wikipedia.org/wiki/"
        year = videotitle
        url += year + "_in_India"
        r = requests.get(url)  # sending request to the html document
        soup = bs(r.content, 'lxml')  # parsing the html doc
        tagDoc = soup.find("div", {"class": "mw-parser-output"}) 
        details=tagDoc.text    
        context = {'form': details}

    return render(request,'website/search.html',context)

def home(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)

        if form.is_valid():
            return redirect('search')
    else:
        form = VideoForm()

    context = {'form':form}

    return render(request,'website/home.html', context)