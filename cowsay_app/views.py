from django.shortcuts import render, HttpResponseRedirect
from cowsay_app.forms import CowsayForm

# Create your views here.

def index(request):
  return render(request, 'index.html', {'form': form})


def history(request):
  return render(request, 'history.html', {'form': form})
