from django.shortcuts import render, HttpResponse, redirect
from myapp.models import *
from django.contrib import messages
from django.http import FileResponse, JsonResponse
from django.db import connections



# Home & Master

def home(request):
    return render(request, 'home.html')

def rawtodict(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def form_index(request):   
    if request.method == 'POST':  
        Person.objects.create(first_name=request.POST['first_name'], 
        last_name=request.POST['last_name'], dob=request.POST['dob'], 
        email=request.POST['email'], file=request.FILES['attach'], 
        shift=request.POST['shift'],stime=request.POST['stime'], etime=request.POST['etime'],
        created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(),
        )
        messages.success(request, "Data Added Successfully" )
        return redirect('/form_index/')

    query_results = Person.objects.all()
    return render(request, 'myapp/form_index.html', {'query_results':query_results})



def form_edit(request,id):
    if request.method == 'POST':
        data1 = Person.objects.filter(id=id).update(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dob=request.POST['dob'], email=request.POST['email'])
        messages.info(request, "Data Added Successfully" )
        return redirect('/form_index/')

    data = Person.objects.get(id=id)
    return render(request,'myapp/form_edit.html',{'data':data})


def form_delete(request,id):   
        Person.objects.filter(id=id).delete()
        messages.error(request, "Data Added Successfully" )
        return redirect('/form_index/')


def shift_index(request):
    if request.method == 'POST':  
        Shift.objects.create(shift_name=request.POST['shift_name'], stime=request.POST['stime'], etime=request.POST['etime'])
        messages.success(request, "Data Added Successfully" )
        return redirect('/shift_index/')
        
    query_results = Shift.objects.all()
    return render(request, 'myapp/shift_index.html',{'query_results':query_results})


def getshift(request):
    form = Shift(request.GET.get('def'))
    data = request.GET.get('def')
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * FROM myapp_shift WHERE shift_name = '%s'" % data)
    r=rawtodict(cursor)
    compact={'data': 'Hii'}
    return JsonResponse(compact)


def demo_form_index(request):
    if request.method == 'POST':  
         Test.objects.create(user_id=request.POST['user_id'])
         messages.success(request, "Data Added Successfully" )

    return render(request, 'myapp/demo_form_index.html')

def user_form_index(request):  
    if request.method == 'POST':
        User.objects.create(user_id=request.POST['user_id'], name=request.POST['name'], division=request.POST['division'], address=request.POST['address'])
        messages.success(request, "Data Added Successfully" )
        return redirect('/user_form_show/')

    primary_values = Test.objects.all()
    compact = {'primary_values': primary_values}


    return render(request, 'myapp/user_form_index.html', compact)


def user_form_show(request):

    data = Test.objects.filter(id='1', user__user_id='1').all()

    compact = {'data': data}

    return render(request, 'myapp/user_form_show.html', compact)























    


