from django.http import HttpResponse
from django.shortcuts import render

from .models import Bb

def index(request) :
	abbs=Bb.objects.all()
	return render(request,'ind.html',{'abbs':abbs})