from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import yearSearch
import sys
from . import script

# Create your views here.
def search(request):
    if request.method == 'POST':
        videotitle=request.POST['videoname']
        x = script.date(videotitle)
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