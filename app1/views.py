from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    obj = Home.objects.all()
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        roll_no = data.get('roll_no')
        department = data.get('department')
        year = data.get('year')
        
        Home.objects.create(
            name = name,
            roll_no = roll_no,
            department = department,
            year = year,
        )
        return redirect('/')
    context = {'obj' : obj}
    return render(request, 'home.html',context)

def info(request):
    obj = Home.objects.all()
    if request.GET.get('search'):
        obj = obj.filter(name__icontains = request.GET.get('search'))
    context = {'obj' : obj }
    return render(request, 'info.html',context)

def delete(request, id):
    obj = Home.objects.get(id=id)
    obj.delete()
    return redirect('/info/')

def update(request, id):
    obj = Home.objects.get(id=id)
    context = {'obj' : obj }
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        roll_no = data.get('roll_no')
        department = data.get('department')
        year = data.get('year')

        obj.name = name
        obj.roll_no = roll_no
        obj.department = department
        obj.year = year
        obj.save()
        return redirect('/info/')
    return render(request, 'update.html', context)
