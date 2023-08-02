from django.shortcuts import render, HttpResponse, redirect
from myapp.models import *
from django.contrib import messages
from django.http import FileResponse
from django.db import connections




# Create your views here.

def index(request):
    return HttpResponse('Hello World')

def test_index(request):
    return render(request, 'myapp/test.html')

def test_index1(request):
    return render(request, 'myapp/test1.html')

def form_index(request):   
    if request.method == 'POST':  
        Person.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dob=request.POST['dob'], email=request.POST['email'], country=request.POST['country'], file=request.FILES['attach'])
        messages.success(request, "Data Added Successfully" )
        return redirect('/form_index/')

    query_results = Person.objects.all()
    return render(request, 'myapp/form_index.html', {'query_results':query_results})

def form_edit(request,id):
    if request.method == 'POST':
        data1 = Person.objects.filter(id=id).update(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dob=request.POST['dob'], email=request.POST['email'], country=request.POST['country'],file=request.FILES['attach'])
        return redirect('/form_index/')

    data = Person.objects.get(id=id)
    return render(request,'myapp/form_edit.html',{'data':data})


def test_form(request):
    if request.method == 'POST':       
        Person.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
        return redirect('/form_index/')

    return render(request, 'myapp/form_elements.html')

def form_delete(request,id):   
        Person.objects.filter(id=id).delete()
        return redirect('/form_index/')


def form_download_file(request, id):
    obj = Person.objects.get(id=id)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    response['Content-Disposition'] = "attachment; filename=%s" % obj.file
    return response
    


