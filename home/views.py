from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from.models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message has been sent! our customer serverce Team would be with you shortly')
            return redirect('index')

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    context ={
        'setting':setting,
        'form':form,
    }
    return render(request,'index.html',context)

def page2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message has been sent! our customer serverce Team would be with you shortly')
            return redirect('/index')

    setting = Setting.objects.get(pk=1)
    images = Images.objects.get(pk=1)
    context ={
        'setting':setting,
        'images':images,
    }
    return render(request,'page2.html',context)

def page3(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message has been sent! our customer serverce Team would be with you shortly')
            return redirect('/index')
            
    setting = Setting.objects.get(pk=1)
    images = Images.objects.get(pk=1)
    context ={
        'setting':setting,
        'images':images,
    }
    return render(request,'page3.html',context)