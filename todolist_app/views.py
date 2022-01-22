from django.shortcuts import render
from todolist_app.models import List

from . forms import ListForm

# Create your views here.

def home(request):
    """home page of todolist app"""
    lists = List.objects.all()
    if request.method != 'POST':
        form = ListForm()
    else:
        form  =  ListForm(request.POST)
        if form.is_valid:
            form.save
    context = {'lists': lists, 'form':form}
    return render(request, 'todolist_app/home.html', context)

