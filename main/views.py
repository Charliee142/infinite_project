from django.shortcuts import render, redirect, HttpResponseRedirect
from main.models import *


def index(request):
    projects = Project.objects.all()[0:3]

    
    context = {
        'projects': projects,
    }
    return render(request, 'main/index.html', context)


def Portfolio(request):
    projects = Project.objects.all()
   
    context = {
        'projects': projects
    }
    return render(request, 'main/portfolio.html',  context)


def Portfolio_detail(request, slug):
    project = Project.objects.get(slug=slug)

    context = {
        'project': project,
    }
    return render(request, 'main/portfolio_detail.html', context)

def about(request):
    return render(request, 'main/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact = Contact(
            name = name,
            email = email,
            message = message,    
        )
        contact.save()
        return redirect('index')
    return render(request, 'main/contact.html')