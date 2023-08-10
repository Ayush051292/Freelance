from django.shortcuts import render, HttpResponse, redirect
from freelance.models import *
from django.contrib import messages
from django.db.models import Sum
import locale
from datetime import datetime
# import datetime
import calendar
from django.http import FileResponse, JsonResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User


# Main Form Start 


def home(request):
    return render(request, 'home.html')

def master(request):
    return render(request, 'master.html')

@login_required(login_url = "/user_login")
def dashboard(request):
    return render(request, 'dashboard.html')

def masterpage(request):
    return render(request, 'masterpage.html')

def user_register(request):
    if request.method == 'POST':
        u = User.objects.create(username = request.POST['username'])
        u.set_password(request.POST['password'])
        u.save()
        return redirect('/user_login')
    return render(request, 'login/register.html')


def user_login(request):
    if request.method == 'POST':
        if User.objects.filter(username = request.POST['username']).exists():
            user = authenticate(request, username = request.POST['username'], password = request.POST['password'])

            if user is None:
                messages.error(request, 'Wrong Password Given')
                return redirect('/user_login')
            else:
                login(request, user)
                return redirect('/')
        messages.error(request, 'Wrong Password Given')
        return redirect('/user_login')


    return render(request, 'login/login.html')


def user_logout(request):
    logout(request)
    return redirect('/user_login')
    




# Payment Type

@login_required(login_url = "/user_login")
def paytypeindex(request):
    now = datetime.now()
    if request.method == 'POST':
        Paymenttype.objects.create(payment_type = request.POST['payment_type'],
             created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
             updated_at = now.strftime("%Y-%m-%d %H:%M:%S"))
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/paytypeindex/')
        
    mydata = Paymenttype.objects.all().values()
    context = {'paytypes': mydata,}
    
    return render(request,'paymenttypes/index.html',context)

@login_required(login_url = "/user_login")
def pay_update(request, id):
    now = datetime.now()
    Paymenttype.objects.filter(id=id).update(payment_type = request.POST['payment_type'],updated_at = now.strftime("%Y-%m-%d %H:%M:%S"))
    messages.info(request, 'Data Submitted Successfully')
    return redirect('/paytypeindex/')  


@login_required(login_url = "/user_login")
def pay_delete(request, id):
    Paymenttype.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/paytypeindex/')


# Payment Mode
@login_required(login_url = "/user_login")
def paymodeindex(request):
    now = datetime.now()
    if request.method == 'POST':
        Paymentmode.objects.create(payment_mode = request.POST['payment_mode'], created_at = now.strftime("%Y-%m-%d %H:%M:%S"), updated_at = now.strftime("%Y-%m-%d %H:%M:%S"))
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/paymodeindex/')
        
    mydata = Paymentmode.objects.all().values()
    context = {'paymodes': mydata}
    
    return render(request,'paymentmodes/index.html',context)

@login_required(login_url = "/user_login")
def paymode_update(request, id):
    now = datetime.now()
    Paymentmode.objects.filter(id=id).update(payment_mode = request.POST['payment_mode'],updated_at = now.strftime("%Y-%m-%d %H:%M:%S"))
    messages.info(request, 'Data Submitted Successfully')
    return redirect('/paymodeindex/')  

@login_required(login_url = "/user_login")
def paymode_delete(request, id):
    Paymentmode.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/paymodeindex/')


# Payment To Bank
@login_required(login_url = "/user_login")
def payindex(request):
    now = datetime.now()
    banks1 = Paymentmode.objects.all()
    
    banks = {'bank_data': banks1}
    
    if request.method == 'POST':
            
        Paymentobank.objects.create(payment_to_bank = request.POST['payment_to_bank'],
            payroll = request.POST['payroll'],
            bank_name = request.POST['bank_name'],
            account_no = request.POST['account_no'],
            branch = request.POST['branch'],
            pan = request.POST['pan'],
            created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
            updated_at = now.strftime("%Y-%m-%d %H:%M:%S"))
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/payindex/',banks)
    
    mydata = Paymentobank.objects.all().values()
    context = {'paybanks': mydata}
  
    return render(request,'paymentobanks/index.html',context)

@login_required(login_url = "/user_login")
def paybank_update(request, id):
    now = datetime.now()
    Paymentobank.objects.filter(id=id).update(payment_to_bank = request.POST['payment_to_bank'],
             payroll = request.POST['payroll'],
             bank_name = request.POST['bank_name'],
             account_no = request.POST['account_no'],
             branch = request.POST['branch'],
             pan = request.POST['pan'],
             updated_at = now.strftime("%Y-%m-%d %H:%M:%S"))
    messages.info(request, 'Data Submitted Successfully')
    return redirect('/payindex/')

@login_required(login_url = "/user_login")
def paybank_delete(request, id):
    Paymentobank.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/payindex/')  

# Company
@login_required(login_url = "/user_login")
def company_index(request):
    companies = Companies.objects.all() 
    return render(request, 'companies/index.html', {'companies':companies})

@login_required(login_url = "/user_login")
def company_create(request):
    now = datetime.now()

    if request.method=='POST':
        payroll = request.POST['payroll']
        pandeduct = request.POST['pandeduct']
        tandeduct = request.POST['tandeduct']
        address = request.POST['address']
        gstn = request.POST['gstn']
        max_emp = request.POST['max_emp']
        max_crm = request.POST['max_crm']
        clogo = request.FILES['clogo']
        email = request.POST['email']
        phone = request.POST['phone']
        regno = request.POST['regno']
        trade_license = request.POST['trade_license']
        created_at = now.strftime("%Y-%m-%d %H:%M:%S")
        updated_at = now.strftime("%Y-%m-%d %H:%M:%S")

        

        Companies.objects.create(payroll=payroll, pandeduct=pandeduct, 
                                 tandeduct=tandeduct, address=address, 
                                 gstn=gstn, created_at=created_at, 
                                 updated_at=updated_at, clogo = clogo,
                                 max_crm = max_crm, max_emp = max_emp,
                                 email=email, phone = phone,
                                 regno = regno, trade_license = trade_license)
        
        
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/company_index/')
    return render(request, 'companies/create.html')

@login_required(login_url = "/user_login")
def company_edit(request, id):
    now = datetime.now()
    companies = Companies.objects.get(id=id)
    if request.method=='POST':
        payroll = request.POST['payroll']
        pandeduct = request.POST['pandeduct']
        tandeduct = request.POST['tandeduct']
        address = request.POST['address']
        gstn = request.POST['gstn']
        max_emp = request.POST['max_emp']
        max_crm = request.POST['max_crm']
        clogo = request.FILES['clogo']
        email = request.POST['email']
        phone = request.POST['phone']
        regno = request.POST['regno']
        trade_license = request.POST['trade_license']
        updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
        Companies.objects.filter(id=id).update(payroll=payroll, pandeduct=pandeduct, 
                                               tandeduct=tandeduct, address=address, 
                                               gstn=gstn, updated_at=updated_at,
                                               clogo = clogo,max_crm = max_crm, 
                                               max_emp = max_emp,email=email, 
                                               phone = phone,regno = regno, 
                                               trade_license = trade_license)
                                               
        messages.info(request, 'Data Submitted Successfully')
        return redirect('/company_index/')
    return render(request, 'companies/edit.html', {'companies':companies})

@login_required(login_url = "/user_login")
def company_delete(request, id):
    Companies.objects.get(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/company_index/')


# Currency
@login_required(login_url = "/user_login")
def currency_index(request):
    currencies = Currencies.objects.all()
    return render(request, 'currencies/index.html', {'currencies':currencies})

@login_required(login_url = "/user_login")
def currency_create(request):
    now = datetime.now()
    if request.method=='POST':
        currency = request.POST['currency']
        rate = request.POST['rate']
        created_at = now.strftime("%Y-%m-%d %H:%M:%S")
        updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
        Currencies.objects.create(currency=currency, rate=rate, created_at=created_at, updated_at=updated_at)
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/currency_index')
    return render(request, 'currencies/create.html')

@login_required(login_url = "/user_login")
def currency_edit(request, id):
    now = datetime.now()
    currencies = Currencies.objects.get(id=id)
    if request.method=='POST':
        currency = request.POST['currency']
        rate = request.POST['rate']
        updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
        Currencies.objects.filter(id=id).update(currency=currency, rate=rate, updated_at=updated_at)
        messages.info(request, 'Data Submitted Successfully')
        return redirect('/currency_index')
    return render(request, 'currencies/edit.html', {'currencies':currencies})

@login_required(login_url = "/user_login")
def currency_delete(request, id):
    Currencies.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/currency_index')


# Month
@login_required(login_url = "/user_login")
def month_index(request):
    months = Month.objects.all()
    return render(request, 'months/index.html', {'months':months})

@login_required(login_url = "/user_login")
def month_create(request):
    now = datetime.now()
    if request.method=='POST':
        month = request.POST['month']
        created_at = now.strftime("%Y-%m-%d %H:%M:%S")
        updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
        Month.objects.create(month=month, created_at=created_at, updated_at=updated_at)
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/month_index/')
    return render(request, 'months/create.html')

@login_required(login_url = "/user_login")
def month_edit(request, id):
    now = datetime.now()
    months = Month.objects.get(id=id)
    if request.method=='POST':
        month = request.POST['month']
        updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
        Month.objects.filter(id=id).update(month=month, updated_at=updated_at)
        messages.info(request, 'Data Submitted Successfully')
        return redirect('/month_index/')
    return render(request, 'months/edit.html', {'months':months})

@login_required(login_url = "/user_login")
def month_delete(request, id):
    Month.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/month_index/')


# Job Detail

@login_required(login_url = "/user_login")
def jobindex(request):
    now = datetime.now()
    if request.method == 'POST':
        Jobdetail.objects.create(crm = request.POST['crm'],
            job_id = request.POST['job_id'],
            words = int(request.POST['words']),
            value = int(request.POST['value']),
            ppw = request.POST['ppw'],
            currency = request.POST['currency'],
            value_inr = int(request.POST['value_inr']),
            participant = request.POST['participant'],
            created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
            updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
            )
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/jobindex/')
    
    mydata = Jobdetail.objects.all().values()
    currencies = Currencies.objects.all()
    context = {'jobdetails': mydata,'currencies': currencies}
    
    return render(request,'jobdetails/index.html',context)

@login_required(login_url = "/user_login")
def job_update(request, id):
    now = datetime.now()
   
    Jobdetail.objects.filter(id=id).update(crm = request.POST['crm'],
                                           job_id = request.POST['job_id'],
                                           words = request.POST['words'],
                                           value = request.POST['value'],
                                           ppw = request.POST['ppw'],
                                           currency = request.POST['currency'],
                                           value_inr = int(request.POST['value_inr']),
                                           participant = request.POST['participant'],
                                           updated_at = now.strftime("%Y-%m-%d %H:%M:%S"))
 

    messages.info(request, 'Form Updated successful')
    return redirect('/jobindex/')  

@login_required(login_url = "/user_login")
def job_delete(request, id):
    Jobdetail.objects.filter(id=id).delete()
    messages.error(request, 'Form Deleted successful')
    return redirect('/jobindex/')

def formatINR(number):
    number = float(number)
    number = round(number)
    is_negative = number < 0
    number = abs(number)
    s, *d = str(number).partition(".")
    r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
    value = "".join([r] + d)
    if is_negative:
       value = '-' + value
    return value

@login_required(login_url = "/user_login")
def job_report(request):
    today = datetime.now()
    year_month = today.strftime("%Y-%m")
    year_month_name = today.strftime("%B_%Y")



    if request.method == 'POST':
        search_mon_year = request.POST['mon']
        month = search_mon_year.split('_')[0]
        year = search_mon_year.split('_')[1]
        month_num = datetime.strptime(month, '%B').month

        if month_num<10:
            month_val='0'+str(month_num)
        else:
            month_val= month_num

        year_month = str(year)+'-'+str(month_val)

        year_month_name = calendar.month_name[month_num]+'_'+year   
        
        



 
 
# dates of july  2020


    months = Month.objects.all()
    total_crm_count = len(Jobdetail.objects.filter(created_at__startswith=year_month).values('crm').distinct())
    total_words=Jobdetail.objects.filter(created_at__startswith=year_month).aggregate(total_words=Sum('words'))['total_words'] or 0
    total_values=Jobdetail.objects.filter(created_at__startswith=year_month).aggregate(total_values=Sum('value_inr'))['total_values'] or 0
    all_crm = Jobdetail.objects.filter(created_at__startswith=year_month).values('crm').distinct()

    final_data = []
    for crm_name in all_crm:
        res = {}
        res['crm_name'] = crm_name['crm']
        res['crm_word'] = formatINR(Jobdetail.objects.filter(crm = crm_name['crm'], created_at__startswith=year_month).aggregate(crm_word=Sum('words'))['crm_word'] or 0)

        res['total_values'] = formatINR(Jobdetail.objects.filter(crm = crm_name['crm'], created_at__startswith=year_month).aggregate(total_values=Sum('value_inr'))['total_values'] or 0)
        
        if res['total_values'] != '0' and  res['crm_word'] != 0:
            final_data.append(res)

    total_crm_words = 0
    total_crm_value = 0

    compact= {'total_crm_count': total_crm_count, 
              'total_words': formatINR(total_words),
              'total_values': formatINR(total_values),
              'final_data':final_data,
              'months': months,
              'year_month_name':year_month_name,
              'total_crm_words': total_crm_words,
              'total_crm_value': total_crm_value,}



    return render(request,'jobdetails/job_report.html', compact)

@login_required(login_url = "/user_login")
def job_report_search(request):
    search_mon_year = request.POST['mon']
    month = search_mon_year.split('_')[0]
    year = search_mon_year.split('_')[1]

    month_num = datetime.strptime(month, '%B').month
    
    if month_num < 10:
        month_val = '0' + str(month_num) 
    else:
        month_val = month_num

    year_month = year+'-'+month_val

    months = Month.objects.all()
    total_crm_count = len(Jobdetail.objects.filter(created_at__startswith=year_month).values('crm').distinct())
    total_words=Jobdetail.objects.filter(created_at__startswith=year_month).aggregate(total_words=Sum('words'))['total_words'] or 0
    total_values=Jobdetail.objects.filter(created_at__startswith=year_month).aggregate(total_values=Sum('value_inr'))['total_values'] or 0
    all_crm = Jobdetail.objects.filter(created_at__startswith=year_month).values('crm').distinct()

    final_data = []
    for crm_name in all_crm:
        res = {}
        res['crm_name'] = crm_name['crm']
        res['crm_word'] = formatINR(Jobdetail.objects.filter(crm = crm_name['crm'], created_at__startswith=year_month).aggregate(crm_word=Sum('words'))['crm_word'] or 0)
        res['total_values'] = formatINR(Jobdetail.objects.filter(crm = crm_name['crm'], created_at__startswith=year_month).aggregate(total_values=Sum('value_inr'))['total_values'] or 0)
        final_data.append(res)
    
    compact= {'total_crm_count': total_crm_count, 
              'total_words': formatINR(total_words),
              'total_values': formatINR(total_values),
              'final_data':final_data,
              'months': months,
              'year_month': year_month,
              'search_mon_year': search_mon_year}


    return render(request,'jobdetails/job_report_search.html', compact)



# Country 
@login_required(login_url = "/user_login")
def country_index(request):
    country = Country.objects.all()
    compact={'country': country}
    now = datetime.now()

    if request.method == 'POST':
        Country.objects.create(country_name=request.POST['country_name'],
                                created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                updated_at = now.strftime("%Y-%m-%d %H:%M:%S"))         

        
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/countries/')
    return render(request,'countries/index.html', compact)

@login_required(login_url = "/user_login")
def country_show(request,id):
    country=Country.objects.get(id=id)
    compact={'data': country}
    return render(request,'countries/country_show.html',compact)

@login_required(login_url = "/user_login")
def country_delete(request,id):
    Country.objects.filter(id=id).delete()
    messages.error(request, "Deleted Successfully")
    return redirect('/countries/')  

@login_required(login_url = "/user_login")
def country_edit(request,id):
    now = datetime.now()
    Country.objects.filter(id=id).update(country_name=request.POST['country_name'],updated_at = now.strftime("%Y-%m-%d %H:%M:%S"))
    messages.info(request, 'Data Edited Successfully')
    return redirect('/countries/')  






# CRM
@login_required(login_url = "/user_login")
def crm_index_form(request):
    crm = Crm.objects.all()
    payment_type=Paymenttype.objects.all()
    payment_mode=Paymentmode.objects.all()
    bank=Paymentobank.objects.all()
    company=Companies.objects.all()
    currency=Currencies.objects.all()
    country=Country.objects.all()


    if request.method == 'POST':
        Crm.objects.create(crm_name=request.POST['crm_name'],crm_number=request.POST['crm_number'],
                            country_id=request.POST['country'],payment_mode_id=request.POST['payment_mode'],
                            payment_type_id=request.POST['payment_type'],currency_id=request.POST['currency'],
                            company_id=request.POST['company'],bank_id=request.POST['bank'],
                            mobile=request.POST['mobile'],contact_email=request.POST['contact_email'],
                            inv_email=request.POST['inv_email'],per_word_rate_mother=request.POST['per_word_rate_mother'],
                            per_word_rate_inr=request.POST['per_word_rate_inr'],credit_limit=request.POST['credit_limit'],
                            gst=request.POST['gst'],tds=request.POST['tds'])

        messages.success(request, 'Data Submitted Successfully')
        return redirect('/crm_index/')


    compact={'payment_type': payment_type,'payment_mode':payment_mode,
             'bank':bank,'company':company,'currency':currency,
             'country':country,'crm': crm}


    return render(request,'crm/crm_index_form.html', compact)

@login_required(login_url = "/user_login")
def crm_edit(request, id):
    now = datetime.now()

    if request.method == 'POST':

        # return HttpResponse(request)
        Crm.objects.filter(id=id).update(crm_name=request.POST['crm_name'],crm_number=request.POST['crm_number'],country=request.POST['country'],payment_mode=request.POST['payment_mode'],payment_type=request.POST['payment_type'],currency=request.POST['currency'],company=request.POST['company'],bank=request.POST['bank'],mobile=request.POST['mobile'],contact_email=request.POST['contact_email'],inv_email=request.POST['inv_email'],per_word_rate_mother=request.POST['per_word_rate_mother'],per_word_rate_inr=request.POST['per_word_rate_inr'],credit_limit=request.POST['credit_limit'],gst=request.POST['gst'],tds=request.POST['tds'],updated_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        messages.info(request, 'Data Submitted Successfully')
        return redirect('/crm_index/')

    data_all=Crm.objects.get(id=id)
    payment_mode=Paymentmode.objects.filter(id=data_all.payment_mode_id).values("payment_mode")[0]['payment_mode']
    payment_type=Paymenttype.objects.filter(id=data_all.payment_type_id).values("payment_type")[0]['payment_type']
    bank=Paymentobank.objects.filter(id=data_all.bank_id).values("payment_to_bank")[0]['payment_to_bank']
    company=Companies.objects.filter(id=data_all.company_id).values("payroll")[0]['payroll']
    currency=Currencies.objects.filter(id=data_all.currency_id).values("currency")[0]['currency']
    country=Country.objects.filter(id=data_all.country_id).values("country_name")[0]['country_name']
    payment_mode1=Paymentmode.objects.all()
    payment_type1=Paymenttype.objects.all()
    bank1=Paymentobank.objects.all()
    company1=Companies.objects.all()
    currency1=Currencies.objects.all()
    country1=Country.objects.all()
    compact={'data':data_all,'payment_mode': payment_mode,
             'payment_type':payment_type,'bank':bank,
             'company':company,'currency':currency,
             'country':country,'payment_mode1': payment_mode1,
             'payment_type1':payment_type1,'bank1':bank1,
             'company1':company1,'currency1':currency1,
             'country1':country1}

    return render(request,'crm/crm_edit_form.html', compact)

   




@login_required(login_url = "/user_login")
def crm_delete(request,id):
    Crm.objects.filter(id=id).delete()
    messages.error(request, "Deleted Successfully")
    return redirect('/crm_index/')


