from django.shortcuts import render
from .models import CowsayModel
from .forms import CowsayForm

import subprocess

# The solution here was gained by reading the provided Kenzie Documentation
# as well as stackoverflow and working out the kinks
def index(request):
  output = ''
  if request.method == 'POST':
    form = CowsayForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      CowsayModel.objects.create(text=data.get('text'))
      text = data.get('text')
      output = subprocess.check_output(['cowsay', text], text=True)
  form = CowsayForm()
  return render(request, 'index.html', {'form': form, 'output': output})

# To find the recent 10 in the datatbase, an order_by needed to create a negative
# This was found in https://code.djangoproject.com/ticket/13089 thank you
# David Cramer from a 10 year old post.
def history_detail(request):
  data = CowsayModel.objects.all().order_by('-id')[:10]
  return render(request, 'history.html', {"data": data})
