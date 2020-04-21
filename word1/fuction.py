from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    text1=request.GET['text']
    text= len(request.GET['text'])
    
    return render(request,'count.html',context={'text': text, 'text1': text1})