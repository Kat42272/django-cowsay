from django.shortcuts import render, HttpResponseRedirect
# from cowsay_app.forms import CowsayForm


def index(request):
  return render(request, 'index.html')


def history(request):
  return render(request, 'history.html')
