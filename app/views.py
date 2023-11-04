from django.shortcuts import render, redirect

from app.models import Contact


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        message = request.POST.get('message')
        contact = Contact(name=name, number=number, message=message)
        contact.save()
        return redirect('index')
    return render(request, 'wash/index.html')
