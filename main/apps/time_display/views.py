from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
  context = {
      "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  print str(context)
  return render(request, 'temp/index.html', context)
