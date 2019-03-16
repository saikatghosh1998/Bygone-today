from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import yearSearch
import sys
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.
def search(request):
    if request.method == 'POST':
        form = yearSearch(request.POST)
        videotitle=request.POST['videoname']

        url = "https://en.wikipedia.org/wiki/"
        year = videotitle
        url += year + "_in_India"
        html = requests.get(url)
        soup = bs(html.content,'lxml')
        container = soup.find('div', {'class':'mw-content-ltr'})
        alList = container.findAll('ul')[7]
        data = alList.select('li')
        x=[]
        for d in data:
            x.append(d.text.strip())
        
        context = {'detail': x}

    return render(request,'website/search.html',context)

def home(request):
    if request.method == 'POST':
        form = yearSearch(request.POST)

        if form.is_valid():
            return redirect('search')
    else:
        form = yearSearch()

    context = {'form':form}

    return render(request,'website/home.html', context)