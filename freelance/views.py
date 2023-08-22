from django.shortcuts import render, HttpResponse, redirect
from freelance.models import *
from django.contrib import messages
from django.db.models import Sum,Q
import locale
from datetime import datetime
# import datetime
import calendar
from django.http import FileResponse, JsonResponse
from .forms import TermconditionForm

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

@login_required(login_url = "/user_login")
def masterpage(request):
    paymentobanks = Paymentobank.objects.count()
    Paymenttypes = Paymenttype.objects.count()
    Currency = Currencies.objects.count()
    Months = Month.objects.count()
    Paymentmodes = Paymentmode.objects.count()
    Company = Companies.objects.count()
    Countries = Country.objects.count()
    Crms = Crm.objects.count()
    emplevels = Emplevel.objects.count()
    customlevels = Custlevel.objects.count()
    cmfmaster = Cmfmaster.objects.count()
    teammaster = Teammaster.objects.count()
    nullpaymenttobank1 = Paymentobank.objects.filter(Q(payment_to_bank=False) | Q(payroll=False) | Q(bank_name=False) | Q(account_no=False) | Q(branch=False) | Q(pan=False) | Q(ifsc=False) | Q(swift_code=False)).count()
    nullpaymenttobank = paymentobanks-nullpaymenttobank1
    nullpaymenttype1 = Paymenttype.objects.filter(Q(payment_type=False) | Q(payroll=False) | Q(bank=False) | Q(status=False)).count()
    nullpaymenttype = Paymenttypes-nullpaymenttype1
    nullcurrency1 = Currencies.objects.filter(Q(rate=False) | Q(currency=False)).count()
    nullcurrency = Currency-nullcurrency1
    nullmonth1 = Month.objects.filter(Q(month=False)).count()
    nullmonth = Months-nullmonth1
    nullpaymentmode1 = Paymentmode.objects.filter(Q(payment_mode=False) | Q(p_order=False) | Q(max_allocation=False) | Q(display_name=False)).count()
    nullpaymentmode = Paymentmodes-nullpaymentmode1
    nullcompany1 = Companies.objects.filter(Q(payroll=False) | Q(pandeduct=False) | Q(tandeduct=False) | Q(address=False) | Q(gstn=False) | Q(max_emp=False) | Q(max_crm=False) | Q(clogo=False) | Q(email=False) | Q(phone=False) | Q(regno=False) | Q(trade_license=False)).count()
    nullcompany = Company-nullcompany1
    nullcountry1 = Country.objects.filter(Q(country_name=False)).count()
    nullcountry = Countries-nullcountry1
    nullcrm1 = Crm.objects.filter(Q(crm_name=False) | Q(crm_number=False) | Q(payment_type=False) | Q(payment_mode=False) | Q(per_word_rate_mother=False) | Q(per_word_rate_inr=False) | Q(currency=False) | Q(country=False) | Q(company=False) | Q(bank=False) | Q(credit_limit=False) | Q(gst=False) | Q(tds=False) | Q(inv_email=False) | Q(contact_email=False) | Q(mobile=False)) .count()
    nullcrm = Crms-nullcrm1
    terms = Termcondition.objects.count()
    nullterms1 = Termcondition.objects.filter(Q(subject=False) | Q(content=False) | Q(type=False)).count()
    nullterms = terms-nullterms1
    nullcmfmaster1 = Cmfmaster.objects.filter(Q(name=False) | Q(type=False)).count()
    nullcmfmaster = cmfmaster-nullcmfmaster1
    nullteammaster1 = Teammaster.objects.filter(Q(team=False) | Q(m_strategy=False) | Q(f_strategy=False)).count()
    nullteammaster = teammaster-nullteammaster1
    nullemplevel1 = Emplevel.objects.filter(Q(level=False) | Q(type=False) | Q(max_word=False) | Q(min_word=False) | Q(monthly_max_word=False) | Q(monthly_min_word=False) | Q(ppw=False) | Q(year=False) | Q(month=False) | Q(date=False)).count() 
    nullemplevel = emplevels-nullemplevel1
    nullcustlevel1 = Custlevel.objects.filter(Q(level=False) | Q(type=False) | Q(max_word=False) | Q(min_word=False) | Q(monthly_max_word=False) | Q(monthly_min_word=False)).count()    
    nullcustlevel = customlevels-nullcustlevel1
    strategymaster = Strategymaster.objects.count()
    nullstrategymaster1 = Strategymaster.objects.filter(Q(strategy=False) | Q(t1=False) | Q(t2=False) | Q(t3=False) | Q(t4=False)).count()
    nullstrategymaster = strategymaster-nullstrategymaster1

    marketingstrategy = Marketingstrategy.objects.count()
    nullmarketingstrategy1 = Marketingstrategy.objects.filter(Q(type=False) | Q(value=False)).count()
    nullmarketingstrategy = marketingstrategy-nullmarketingstrategy1
    location = Location.objects.count()
    nulllocation1 = Location.objects.filter(Q(location=False)).count()
    nulllocation = location-nulllocation1
    
    designation = Designation.objects.count()
    nulldesignation1 = Designation.objects.filter(Q(designation=False)).count()
    nulldesignation = designation-nulldesignation1
    
    announcement = Announcement.objects.count()

   # nulllocation = Location.objects.filter(Q(location=False)).count()
   # nulldesignation = Designation.objects.filter(Q(designation=False)).count()
    return render(request, 'masterpage.html', {'location':location,'nulllocation':nulllocation,'designation':designation,
               'nulldesignation':nulldesignation,'strategymaster':strategymaster,
'nullstrategymaster':nullstrategymaster,
'marketingstrategy':marketingstrategy,
'nullmarketingstrategy':nullmarketingstrategy,
'terms':terms,
'nullterms':nullterms,'nullpaymenttobank': nullpaymenttobank,
'nullpaymenttype':nullpaymenttype,
'nullcurrency':nullcurrency,                
'nullmonth':nullmonth,
'nullpaymentmode':nullpaymentmode,
'nullcompany':nullcompany,
'nullcountry':nullcountry,
'nullcrm':nullcrm,
'nullcmfmaster':nullcmfmaster,
'nullteammaster':nullteammaster,
'nullcustlevel':nullcustlevel,
'nullemplevel':nullemplevel,
'cmfmaster':cmfmaster,
'teammaster':teammaster,
'customlevels':customlevels, 
'emplevels':emplevels,
'paymentobanks':paymentobanks, 'Paymenttypes':Paymenttypes, 'Currency':Currency, 'Months':Months, 
'Paymentmodes':Paymentmodes, 'Company':Company, 'Countries':Countries, 'Crms':Crms,'announcement':announcement})

def user_register(request):
    now = datetime.now()
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        pan=request.POST['pan']
        password=request.POST['password']

        u = User.objects.create(username=email, email=email, first_name=first_name,last_name=last_name)
        u.set_password(password)
        u.save()

        Freelancer.objects.create(auth_user=u,
                                  reported_to=u,
                                  updated_by=u,
                                  email=email,
                                  pan=pan,
                                  location=Location.objects.get(id=1),
                                  role=Role.objects.get(id=1),
                                  department=Companies.objects.get(id=4),
                                  designation=Designation.objects.get(id=1),
                                  status=1,
                                #   doj=datetime.datetime.now().strftime("%Y-%m-%d"),
                                  user_type='Freelancer',
                                  #role='freelancer',
                                  name=first_name+' '+last_name,
                                  created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                  updated_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                  )
        return redirect('/user_login')
    return render(request, '/user_login')

# @login_required(login_url = "/user_login")
def customer_register(request):
    now = datetime.now()
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        pan=request.POST['pan']
        password=request.POST['password']

        u = User.objects.create(username=email, email=email, first_name=first_name,last_name=last_name)
        u.set_password(password)
        u.save()

        Freelancer.objects.create(auth_user=u,
                                  reported_to=u,
                                  updated_by=u,
                                  email=email,
                                  pan=pan,
                                  location=Location.objects.get(id=1),
                                  role=Role.objects.get(id=1),
                                  department=Companies.objects.get(id=1),
                                  designation=Designation.objects.get(id=1),
                                  status=1,
                                  #doj=datetime.datetime.now().strftime("%Y-%m-%d"),
                                  user_type='Customer',
                                  #role='customer',
                                  name=first_name+' '+last_name,
                                  created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                  updated_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                  )
        return redirect('/customer_register')
    return render(request, 'login/customer_register.html')

# @login_required(login_url = "/user_login")
def user_login(request):
    if request.method == 'POST':
        if User.objects.filter(username = request.POST['username']).exists():
            user = authenticate(request, username = request.POST['username'], password = request.POST['password'])

            if user is None:
                messages.error(request, 'Wrong Password Given')
                return redirect('/user_login')
            else:
                login(request, user)
                k=Freelancer.objects.filter(auth_user_id=request.user.id)[0].user_type
                if k=='Freelancer':
                    return redirect('/')    #url of the dashboard for freelancer
                if k=='Customer':
                    return redirect('/')    #url of the dashboard for customer
        messages.error(request, 'Wrong Password Given')
        return redirect('/user_login')
    return render(request, 'login/login.html')


# @login_required(login_url = "/user_login")
def user_logout(request):
    logout(request)
    return redirect('/user_login')
    
@login_required(login_url = "/user_login")
def user_profile(request):
    data = Freelancer.objects.filter(auth_user = request.user.id).all()[0]
    role = Role.objects.all()
    designation = Designation.objects.all()
    department = Companies.objects.all()
    location = Location.objects.all()
    

    main = Freelancer.objects.filter(Q(name='None') | Q(name = '') |
                                     Q(email='None') | Q(email = '') |
                                     Q(phone='None') | Q(phone = '') | 
                                     Q(image='None') | Q(image = '') 
                                    #  Q(role='None') | Q(role = '') 
                                    #  Q(designation='None') | Q(designation = '') |
                                    #  Q(department='None') | Q(department = '') |
                                    #  Q(reported_to='None') | Q(reported_to = '') |
                                    #  Q(location='None') | Q(location = '')
                                     ).filter(auth_user = request.user.id).count()


    personal = Freelancer.objects.filter(Q(aadhar = 'None') | Q(aadhar = '') | Q(aadhar__isnull = True) | 
                                         Q(pan = 'None') | Q(pan = '') |  Q(pan__isnull = True) | 
                                         Q(dob = 'None') | Q(dob = '') |  Q(dob__isnull = True) | 
                                         Q(address = 'None') | Q(pan = '') | Q(address__isnull = True) |  
                                         Q(blood = 'None') | Q(blood = '') | Q(blood__isnull = True) ).filter(auth_user = request.user.id).count()



    work = Freelancer.objects.filter(Q(doj='None') | Q(doj='')| Q(doj__isnull = True) |
                                     Q(user_type='None') |Q(user_type = '') | Q(user_type__isnull = True) |
                                     Q(salary='None') |Q(salary = '') | Q(salary__isnull = True) |
                                     Q(status='None') |Q(status = '')| Q(status__isnull = True)).filter(auth_user = request.user.id).count()
    
    
    
    education = Freelancer.objects.filter(Q(school = 'None')| Q(school = '') | Q(school__isnull = True) |
                                          Q(degree = 'None')| Q(degree = '') | Q(degree__isnull = True) |
                                          Q(university = 'None')| Q(university = '') | Q(university__isnull = True) |
                                          Q(marks = 'None')| Q(marks = '') | Q(marks__isnull = True) |
                                          Q(subject = 'None')| Q(subject = '') | Q(subject__isnull = True)).filter(auth_user = request.user.id).count()
    
    
    
    bank = Freelancer.objects.filter(Q(bank = 'None')| Q(bank = '') | Q(bank__isnull = True) |
                                     Q(accno = '')| Q(accno = '') | Q(accno__isnull = True) |
                                     Q(ifsc = 'None')| Q(ifsc = '')| Q(ifsc__isnull = True) ).filter(auth_user = request.user.id).count()
    
    # Personal

    personal_profile_queryset = Freelancer.objects.annotate(
        aadhar_empty=models.Case(
            models.When(models.Q(aadhar__isnull=True) | models.Q(aadhar="") | models.Q(aadhar="None"), then=1),
            default=0,
        ),
        dob_empty=models.Case(
            models.When(models.Q(dob__isnull=True) | models.Q(dob="") | models.Q(dob="None"), then=1),
            default=0,
        ),
        pan_empty=models.Case(
            models.When(models.Q(pan__isnull=True) | models.Q(pan="") | models.Q(pan="None"), then=1),
            default=0,
        ),
        blood_empty=models.Case(
            models.When(models.Q(blood__isnull=True) | models.Q(blood="") | models.Q(blood="None"), then=1),
            default=0,
        ),
        address_empty=models.Case(
            models.When(models.Q(address__isnull=True) | models.Q(address="") | models.Q(address="None"), then=1),
            default=0,
        ),
        empty_fields_count_personal=(
            models.F("aadhar_empty") + 
            models.F("dob_empty") + 
            models.F("pan_empty") + 
            models.F("blood_empty") + 
            models.F("address_empty") 
        )
    )
    
    personal_profile = personal_profile_queryset.get(auth_user=request.user.id)

    # Personal Information    
    personal_total = 5
    personal_null = personal_profile.empty_fields_count_personal
    personal_fill = personal_total - personal_null
    
    
    
     # Work

    work_profile_queryset = Freelancer.objects.annotate(
        doj_empty=models.Case(
            models.When(models.Q(doj__isnull=True) | models.Q(doj="") | models.Q(doj="None"), then=1),
            default=0,
        ),
        salary_empty=models.Case(
            models.When(models.Q(salary__isnull=True) | models.Q(salary="") | models.Q(salary="None"), then=1),
            default=0,
        ),
        user_type_empty=models.Case(
            models.When(models.Q(user_type__isnull=True) | models.Q(user_type="") | models.Q(user_type="None"), then=1),
            default=0,
        ),
        status_empty=models.Case(
            models.When(models.Q(status__isnull=True) | models.Q(status="") | models.Q(status="None"), then=1),
            default=0,
        ),

        empty_fields_count_work=(
            models.F("doj_empty") + 
            models.F("salary_empty") + 
            models.F("user_type_empty") + 
            models.F("status_empty")
        )
    )
    
    work_profile = work_profile_queryset.get(auth_user=request.user.id)

    # Personal Information    
    work_total = 4
    work_null = work_profile.empty_fields_count_work
    work_fill = work_total - work_null
    
    

     # Education

    education_profile_queryset = Freelancer.objects.annotate(
        school_empty=models.Case(
            models.When(models.Q(school__isnull=True) | models.Q(school="") | models.Q(school="None"), then=1),
            default=0,
        ),
        degree_empty=models.Case(
            models.When(models.Q(degree__isnull=True) | models.Q(degree="") | models.Q(degree="None"), then=1),
            default=0,
        ),
        university_empty=models.Case(
            models.When(models.Q(university__isnull=True) | models.Q(university="") | models.Q(university="None"), then=1),
            default=0,
        ),
        marks_empty=models.Case(
            models.When(models.Q(marks__isnull=True) | models.Q(marks="") | models.Q(marks="None"), then=1),
            default=0,
        ),
        subject_empty=models.Case(
            models.When(models.Q(subject__isnull=True) | models.Q(subject="") | models.Q(subject="None"), then=1),
            default=0,
        ),

        empty_fields_count_education=(
            models.F("school_empty") + 
            models.F("degree_empty") + 
            models.F("university_empty") + 
            models.F("marks_empty") + 
            models.F("subject_empty")
        )
    )
    
    education_profile = education_profile_queryset.get(auth_user=request.user.id)

    # Education Information    
    education_total = 5
    education_null = education_profile.empty_fields_count_education
    education_fill = education_total - education_null
    
    
         # Bank

    bank_profile_queryset = Freelancer.objects.annotate(
        bank_empty=models.Case(
            models.When(models.Q(bank__isnull=True) | models.Q(bank="") | models.Q(bank="None"), then=1),
            default=0,
        ),
        ifsc_empty=models.Case(
            models.When(models.Q(ifsc__isnull=True) | models.Q(ifsc="") | models.Q(ifsc="None"), then=1),
            default=0,
        ),
        accno_empty=models.Case(
            models.When(models.Q(accno__isnull=True) | models.Q(accno="") | models.Q(accno="None"), then=1),
            default=0,
        ),


        empty_fields_count_bank=(
            models.F("bank_empty") + 
            models.F("ifsc_empty") + 
            models.F("accno_empty")
            
        )
    )
    
    bank_profile = bank_profile_queryset.get(auth_user=request.user.id)

    # Bank Information    
    bank_total = 3
    bank_null = bank_profile.empty_fields_count_bank
    bank_fill = bank_total - bank_null



    # Basic

    basic_profile_queryset = Freelancer.objects.annotate(
        image_empty=models.Case(
            models.When(models.Q(image__isnull=True) | models.Q(image="") | models.Q(image="None"), then=1),
            default=0,
        ),
        name_empty=models.Case(
            models.When(models.Q(name__isnull=True) | models.Q(name="") | models.Q(name="None"), then=1),
            default=0,
        ),
        email_empty=models.Case(
            models.When(models.Q(email__isnull=True) | models.Q(email="") | models.Q(email="None"), then=1),
            default=0,
        ),
        phone_empty=models.Case(
            models.When(models.Q(phone__isnull=True) | models.Q(phone="") | models.Q(phone="None"), then=1),
            default=0,
        ),
        role_empty=models.Case(
            models.When(models.Q(role__isnull=True), then=1),
            default=0,
        ),
        reported_to_empty=models.Case(
            models.When(models.Q(reported_to__isnull=True), then=1),
            default=0,
        ),
        location_empty=models.Case(
            models.When(models.Q(location__isnull=True), then=1),
            default=0,
        ),
        designation_empty=models.Case(
            models.When(models.Q(designation__isnull=True), then=1),
            default=0,
        ),
        department_empty=models.Case(
            models.When(models.Q(department__isnull=True), then=1),
            default=0,
        ),
        empty_fields_count_basic=(
            models.F("image_empty") + 
            models.F("name_empty") + 
            models.F("email_empty") + 
            models.F("role_empty") + 
            models.F("reported_to_empty") + 
            models.F("location_empty") + 
            models.F("designation_empty") +
            models.F("department_empty") +
            models.F("phone_empty")
   
            
        )
    )
    
    basic_profile = basic_profile_queryset.get(auth_user=request.user.id)

    # Basic Information    
    basic_total = 9
    basic_null = basic_profile.empty_fields_count_basic
    basic_fill = basic_total - basic_null


    all_total = basic_total + bank_total + education_total + work_total + personal_total
    all_fill = basic_fill + bank_fill + education_fill + work_fill + personal_fill
    
    
    compact = {'data': data,'role': role,
               'designation': designation,
               'department': department,
               'main':main,
               'personal':personal,
               'work':work,
               'education':education,
               'bank':bank,
               'location':location,
               'personal_total':personal_total,
               'personal_null':personal_null,
               'personal_fill':personal_fill,
               'work_total':work_total,
               'work_null':work_null,
               'work_fill':work_fill,
               'education_total':education_total,
               'education_null':education_null,
               'education_fill':education_fill,
               'bank_total':bank_total,
               'bank_null':bank_null,
               'bank_fill':bank_fill,
               'all_total':all_total,
               'all_fill':all_fill
               }
               

    return render(request, 'profile.html', compact)
    



@login_required(login_url = "/user_login")
def user_profile_edit(request, id1, id2):
    now = datetime.now()
   
    if(id2 == 'main'):
        companies1 = Freelancer.objects.filter(id=id1).values()

        companies = Freelancer.objects.get(id=id1)


        # return HttpResponse(companies[0]['image'])
        if request.method=='POST':
            if len(request.FILES)!=0:
                if len(companies1[0]['image'])>0:
                    os.remove(companies1[0]['image'].path)
                    companies.image=request.FILES['image']
                else:
                    companies.image=request.FILES['image']



        # return HttpResponse(request.POST['designation'])
        companies.name = request.POST['name']
        companies.designation_id = request.POST['designation']
        companies.phone = request.POST['phone']
        companies.role_id = request.POST['role']
        companies.department_id = request.POST['department']
        companies.updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
        companies.save()    


        # Freelancer.objects.filter(id=id1).update(
        #     name= request.POST['name'],
        #     designation= request.POST['designation'],
        #     phone= request.POST['phone'],
        #     role= request.POST['role'],
        #     department= request.POST['department'],
        #     image = request.FILES['image']
        # ) 

    elif(id2 == 'personal'):
        Freelancer.objects.filter(id=id1).update(
            aadhar= request.POST['aadhar'],
            pan= request.POST['pan'],
            dob= request.POST['dob'],
            blood= request.POST['blood'],
            address= request.POST['address'],
        ) 

    elif(id2 == 'work'):
        Freelancer.objects.filter(id=id1).update(
            doj= request.POST['doj'],
            salary= request.POST['salary'],
            user_type= request.POST['user_type'],
            status= request.POST['status'],
        ) 

    elif(id2 == 'education'):
        Freelancer.objects.filter(id=id1).update(
            school= request.POST['school'],
            degree= request.POST['degree'],
            university= request.POST['university'],
            subject= request.POST['subject'],
            marks= request.POST['marks'],
        ) 

    elif(id2 == 'bank'):
        Freelancer.objects.filter(id=id1).update(
            bank= request.POST['bank'],
            ifsc= request.POST['ifsc'],
            accno= request.POST['accno'],
        ) 
        
    messages.info(request, 'Data Submitted Successfully')
    return redirect('/user_profile')

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
    company_data = Companies.objects.all()  
    
    if request.method == 'POST':           
        Paymentobank.objects.create(payment_to_bank = request.POST['payment_to_bank'],
            payroll_id = request.POST['payroll'],
            bank_name = request.POST['bank_name'],
            account_no = request.POST['account_no'],
            branch = request.POST['branch'],
            pan = request.POST['pan'],
            swift_code = request.POST['swift_code'],
            ifsc = request.POST['ifsc'],
            created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
            updated_at = now.strftime("%Y-%m-%d %H:%M:%S"))
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/payindex/')
    
    mydata = Paymentobank.objects.all().order_by('-created_at')
    
    
    context = {'paybanks': mydata,'company_data': company_data}
  
    return render(request,'paymentobanks/index.html',context)

@login_required(login_url = "/user_login")
def paybank_update(request, id):
    now = datetime.now()
    Paymentobank.objects.filter(id=id).update(payment_to_bank = request.POST['payment_to_bank'],
             payroll = request.POST['payroll'],
             bank_name = request.POST['bank_name'],
             account_no = request.POST['account_no'],
             branch = request.POST['branch'],
             ifsc = request.POST['ifsc'],
             swift_code = request.POST['swift_code'],
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
        clogo = 'NA'
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
        clogo = 'NA'
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

@login_required(login_url = "/user_login")
def emplevelindex(request):
    
    # return HttpResponse(request)
    now = datetime.now()

    if request.method == 'POST':
        Emplevel.objects.create(level = request.POST['level'],
                                 type = request.POST['type'],
                                 max_word = int(request.POST['max_word']),
                                 min_word = int(request.POST['min_word']),
                                 monthly_max_word = int(request.POST['max_word']) * 4,
                                 monthly_min_word = int(request.POST['min_word']) * 4,
                                 ppw = request.POST['ppw'],
                                 year = request.POST['year'],
                                 month = request.POST['month'],
                                 date = request.POST['date'],
                                 created_by = request.user.id,
                                 created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                 updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
                                 )
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/emplevelindex/')
    
    mydata = Emplevel.objects.order_by('level').all().values()
    context = {
                  'jobdetails': mydata,
              }
    
    
    
    return render(request,'emplevels/index.html',context)

@login_required(login_url = "/user_login")
def level_delete(request, id):
    Emplevel.objects.filter(id=id).delete()
    
    messages.error(request, 'Form Deleted successful')
    return redirect('/emplevelindex/')        

@login_required(login_url = "/user_login")
def level_update(request, id):
    
    now = datetime.now()
    
    
    Emplevel.objects.filter(id=id).update(level = request.POST['level'],
                                           type = request.POST['type'],
                                           max_word = int(request.POST['max_word']),
                                           min_word = int(request.POST['min_word']),
                                           monthly_max_word = int(request.POST['max_word']) * 4,
                                           monthly_min_word = int(request.POST['min_word']) * 4,
                                           ppw = request.POST['ppw'],
                                           edited_by = request.user.id,
                                           year = request.POST['year'],
                                           month = request.POST['month'],
                                           date = request.POST['date'],
                                           updated_at = now.strftime("%Y-%m-%d %H:%M:%S"))
    return redirect('/emplevelindex/')

#  Cust Level

@login_required(login_url = "/user_login")
def custlevelindex(request):
    
    now = datetime.now()

    if request.method == 'POST':
        
        Custlevel.objects.create(level = request.POST['level'],
                                 type = request.POST['type'],
                                 max_word = int(request.POST['max_word']),
                                 min_word = int(request.POST['min_word']),
                                 monthly_max_word = int(request.POST['max_word']) * 4,
                                 monthly_min_word = int(request.POST['min_word']) * 4,
                                 ppw = 0,
                                 year = 0,
                                 month = 0,
                                 date = 0,
                                 created_by = request.user.id,
                                 created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                 updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
                                 )
        
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/custlevelindex/')
    
    mydata = Custlevel.objects.order_by('level').all().values()
    context = {
                  'jobdetails': mydata,
              }
    
    
    
    return render(request,'custlevels/index.html',context)
    
@login_required(login_url = "/user_login")
def custlevel_delete(request, id):
    Custlevel.objects.filter(id=id).delete()
    
    messages.error(request, 'Form Deleted successful')
    return redirect('/custlevelindex/')        

@login_required(login_url = "/user_login")
def custlevel_update(request, id):
    
    now = datetime.now()
    
    Custlevel.objects.filter(id=id).update(level = request.POST['level'],
                                           type = request.POST['type'],
                                           max_word = int(request.POST['max_word']),
                                           min_word = int(request.POST['min_word']),
                                           monthly_max_word = int(request.POST['max_word']) * 4,
                                           monthly_min_word = int(request.POST['min_word']) * 4,
                                           ppw = request.POST['ppw'],
                                           year = request.POST['year'],
                                           month = request.POST['month'],
                                           date = request.POST['date'],
                                           edited_by = request.user.id,
                                           updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
                                           )
 

    messages.info(request, 'Form Updated successful')
    return redirect('/custlevelindex/')  



# Team Master
@login_required(login_url = "/user_login")
def teammaster(request):

    now = datetime.now()
    mydata = Teammaster.objects.all()
    cmf = Cmfmaster.objects.all()
    f_strategy = Strategymaster.objects.all()
    m_strategy = Marketingstrategy.objects.all()
    customer_cmf = Cmfmaster.objects.filter(name='Customer').count()
    management_cmf = Cmfmaster.objects.filter(name='Management').count()
    facw_cmf = Cmfmaster.objects.filter(name='Facw').count()
    teammaster_company1 = Teammaster.objects.values_list('comp1')
    teammaster_company2 = Teammaster.objects.values_list('comp2')
    teammaster_company3 = Teammaster.objects.values_list('comp3')
    # return HttpResponse(teammaster_company)
    company = Companies.objects.exclude(payroll__in = teammaster_company1).exclude(payroll__in = teammaster_company2).exclude(payroll__in = teammaster_company3).all()
    context = {'mydata': mydata,'cmf': cmf, 'f_strategy':f_strategy, 'm_strategy':m_strategy, 'customer_cmf':customer_cmf, 'management_cmf':management_cmf, 'facw_cmf':facw_cmf, 'company':company}

    if request.method == 'POST':
        Teammaster.objects.create(team = request.POST['team'], 
                                f_strategy = request.POST['f_strategy'],
                                m_strategy = request.POST['m_strategy'],
                                comp1 = request.POST['comp1'],
                                comp2 = request.POST['comp2'],
                                comp3 = request.POST['comp3'],
                                created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                created_by = request.user.id,
                            )
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/teammaster/')

    return render(request,'teammasters/index.html',context)

@login_required(login_url = "/user_login")
def teammaster_edit(request, id):
    now = datetime.now()
    Teammaster.objects.filter(id=id).update(team = request.POST['team'], 
                                           f_strategy = request.POST['f_strategy'],
                                           m_strategy = request.POST['m_strategy'],
                                           comp1 = request.POST['comp1'],
                                           comp2 = request.POST['comp2'],
                                           comp3 = request.POST['comp3'],
                                           updated_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                           edited_by = request.user.id,
                                        )
    messages.info(request, 'Data Submitted Successfully')
    return redirect('/teammaster/')  

@login_required(login_url = "/user_login")
def teammaster_delete(request, id):
    Teammaster.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/teammaster/')

def team_company(request, id):
    teammaster_company1 = Teammaster.objects.values_list('comp1')
    teammaster_company2 = Teammaster.objects.values_list('comp2')
    teammaster_company3 = Teammaster.objects.values_list('comp3')
    company = list(Companies.objects.exclude(payroll__in = teammaster_company1).exclude(payroll__in = teammaster_company2).exclude(payroll__in = teammaster_company3).filter(~Q(payroll=id)).values('payroll'))
    # data = company
    # context = {'company':data}
    return JsonResponse({'company':company})

def team_company2(request, id, id1):
    teammaster_company1 = Teammaster.objects.values_list('comp1')
    teammaster_company2 = Teammaster.objects.values_list('comp2')
    teammaster_company3 = Teammaster.objects.values_list('comp3')
    company = list(Companies.objects.exclude(payroll__in = teammaster_company1).exclude(payroll__in = teammaster_company2).exclude(payroll__in = teammaster_company3).filter(~Q(payroll=id)).filter(~Q(payroll=id1)).values('payroll'))
    # data = company
    # context = {'company':data}
    return JsonResponse({'company':company})

def team_company11(request, id):
    teammaster_company1 = Teammaster.objects.values_list('comp1')
    teammaster_company2 = Teammaster.objects.values_list('comp2')
    teammaster_company3 = Teammaster.objects.values_list('comp3')
    company = list(Companies.objects.exclude(payroll__in = teammaster_company1).exclude(payroll__in = teammaster_company2).exclude(payroll__in = teammaster_company3).filter(~Q(payroll=id)).values('payroll'))
    # data = company
    # context = {'company':data}
    return JsonResponse({'company':company})

def team_company22(request, id, id1):
    teammaster_company1 = Teammaster.objects.values_list('comp1')
    teammaster_company2 = Teammaster.objects.values_list('comp2')
    teammaster_company3 = Teammaster.objects.values_list('comp3')
    company = list(Companies.objects.exclude(payroll__in = teammaster_company1).exclude(payroll__in = teammaster_company2).exclude(payroll__in = teammaster_company3).filter(~Q(payroll=id)).filter(~Q(payroll=id1)).values('payroll'))
    # data = company
    # context = {'company':data}
    return JsonResponse({'company':company})



# CMF Master
@login_required(login_url = "/user_login")
def cmfmasterindex(request):
    if request.method == 'POST':
        Cmfmaster.objects.create(name = request.POST['name'], 
                                 type = request.POST['type'],
                                 created_by = request.user.id,
                                 created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                )
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/cmfmaster/')
        
    mydata = Cmfmaster.objects.all().order_by('-created_at')
    context = {'cmfs': mydata}
    
    return render(request,'cmfmasters/index.html',context)

@login_required(login_url = "/user_login")
def cmfmaster_update(request, id):
    Cmfmaster.objects.filter(id=id).update(name = request.POST['name'], 
                                           type = request.POST['type'],
                                           updated_by = request.user.id,
                                           updated_at = now.strftime("%Y-%m-%d %H:%M:%S"),

                                        )
    messages.info(request, 'Data Submitted Successfully')
    return redirect('/cmfmaster/')  

@login_required(login_url = "/user_login")
def cmfmaster_delete(request, id):
    Cmfmaster.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/cmfmaster/')





# Marketing Strategy
@login_required(login_url = "/user_login")
def marketingstrategyindex(request):
    if request.method == 'POST':
        now = datetime.now()
        Marketingstrategy.objects.create(type = request.POST['type'], 
                                 value = request.POST['value'],
                                 created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                 created_by = request.user.id,
                                )
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/marketingstrategy/')
        
    mydata = Marketingstrategy.objects.all().order_by('-created_at')
    context = {'marketingstrategys': mydata}
    
    return render(request,'marketingstrategys/index.html',context)

@login_required(login_url = "/user_login")
def marketingstrategy_update(request, id):
    now = datetime.now()
    Marketingstrategy.objects.filter(id=id).update(type = request.POST['type'], 
                                            value = request.POST['value'],
                                            updated_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                            updated_by = request.user.id,
                                        )
    messages.info(request, 'Data Submitted Successfully')
    return redirect('/marketingstrategy/')  

@login_required(login_url = "/user_login")
def marketingstrategy_delete(request, id):
    Marketingstrategy.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/marketingstrategy/')
    
    
    
# Strategy Master
@login_required(login_url = "/user_login")
def strategymasterindex(request):
    if request.method == 'POST':
        now = datetime.now()
        Strategymaster.objects.create(strategy = request.POST['strategy'], 
                                 t1 = request.POST['t1'],
                                 t2 = request.POST['t2'],
                                 t3 = request.POST['t3'],
                                 t4 = request.POST['t4'],
                                 created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                 created_by = request.user.id,
                                )
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/strategymaster/')
        
    mydata = Strategymaster.objects.all().order_by('-created_at')
    context = {'strategys': mydata}
    
    return render(request,'strategymasters/index.html',context)

@login_required(login_url = "/user_login")
def strategymaster_update(request, id):
    now = datetime.now()
    Strategymaster.objects.filter(id=id).update(strategy = request.POST['strategy'], 
                                            t1 = request.POST['t1'],
                                            t2 = request.POST['t2'],
                                            t3 = request.POST['t3'],
                                            t4 = request.POST['t4'],
                                            updated_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                            updated_by = request.user.id,
                                        )
    messages.info(request, 'Data Submitted Successfully')
    return redirect('/strategymaster/')  

@login_required(login_url = "/user_login")
def strategymaster_delete(request, id):
    Strategymaster.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/strategymaster/')



# Terms & Conditions 

@login_required(login_url = "/user_login")
def termcondition_index(request):
    mydata = Termcondition.objects.all().order_by('-created_at')
    context = {'commons': mydata}
    return render(request,'termconditions/index.html',context)

@login_required(login_url = "/user_login")
def termcondition_create(request):
    form  = TermconditionForm
    now = datetime.now()
    if request.method == 'POST':
        Termcondition.objects.create(type = request.POST['type'], 
                        subject = request.POST['subject'],
                        content = request.POST['content'],
                        created_by = request.user.id,
                        created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                        updated_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                    )
        # form  = TermconditionForm(request.POST)
        # if form.is_valid():
        #     form.save()
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/termcondition_index/')

    return render(request,'termconditions/create.html', {'form':form})

@login_required(login_url = "/user_login")
def termcondition_show(request, id):
    form = Termcondition.objects.get(id = id)

    compact = {'form': form}
    return render(request,'termconditions/show.html', compact)


@login_required(login_url = "/user_login")
def termcondition_edit(request, id):
    data = Termcondition.objects.get(id = id)
    form = TermconditionForm(instance=data)
    compact = {'form': form, 'id': id, 'data': data}
    return render(request,'termconditions/edit.html', compact)


@login_required(login_url = "/user_login")
def termcondition_update(request, id):
    now = datetime.now()
    Termcondition.objects.filter(id=id).update(subject = request.POST['subject'], 
                                           type = request.POST['type'],
                                           content = request.POST['content'],
                                           updated_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                        )
    messages.info(request, 'Data Submitted Successfully')
    return redirect('/termcondition_index/')  



@login_required(login_url = "/user_login")
def termcondition_delete(request, id):
    Termcondition.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/termcondition_index/')


# Location 
@login_required(login_url = "/user_login")
def location_index(request):
    now = datetime.now()
    if request.method == 'POST':
        Location.objects.create(location = request.POST['location'], 
                                 created_by = request.user.id,
                                 created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                 updated_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                )
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/locations/')

    data=Location.objects.all().order_by('-created_at')
    return render(request, "location/index.html", {'data':data})

@login_required(login_url = "/user_login")
def location_edit(request, id):
    now = datetime.now()
    if request.method=='POST':
        Location.objects.filter(id=id).update(location = request.POST['location'],
                                               updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
                                               )
        messages.info(request, 'Data Submitted Successfully')
        return redirect('/locations/')  

@login_required(login_url = "/user_login")
def location_delete(request, id):
    Location.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/locations/')


# Designation
@login_required(login_url = "/user_login")
def designation_index(request):
    now = datetime.now()
    if request.method == 'POST':
        Designation.objects.create(designation = request.POST['designation'], 
                                 created_by = request.user.id,
                                 created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                 updated_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                )
        messages.success(request, 'Data Submitted Successfully')
        return redirect('/designations/')


    data = Designation.objects.all().order_by('-created_at')
    return render(request, "designation/index.html", {'data':data})

@login_required(login_url = "/user_login")
def designation_edit(request, id):
    now = datetime.now()
    if request.method=='POST':
        Designation.objects.filter(id=id).update(designation = request.POST['designation'],
                                               updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
                                               )
        messages.info(request, 'Data Submitted Successfully')
        return redirect('/designations/')  

@login_required(login_url = "/user_login")
def designation_delete(request, id):
    Designation.objects.filter(id=id).delete()
    messages.error(request, 'Data Submitted Successfully')
    return redirect('/designations/')


@login_required(login_url = "/user_login")
def role_index(request):
    if request.method == 'POST':  
        
         Role.objects.create(name=request.POST['name'],
                                 created_by=request.user.id,
                                 created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                 updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                   )
         messages.success(request, "Data Added Successfully")
         
         return redirect('/role_index/')
         
    mydata = Role.objects.all().values()
    context = {'role': mydata}
    
    
    return render(request, 'roles/index.html',context)

@login_required(login_url = "/user_login")
def role_update(request, id):
    
    # return HttpResponse(id)
    
    Role.objects.filter(id=id).update(name = request.POST['name'],
                                             edited_by=request.user.id,
                                             updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
 

    messages.success(request, 'Form submission successful')
    return redirect('/role_index/')  

@login_required(login_url = "/user_login")
def role_delete(request, id):
    
    # return HttpResponse(id)
    
    Role.objects.filter(id=id).delete()
 

    messages.success(request, 'Form Deleted successful')
    return redirect('/role_index/')   


@login_required(login_url = "/user_login")
def permission_index(request):
    if request.method == 'POST':  
        
         Permission.objects.create(permission=request.POST['permission'],
                                 created_by=request.user.id,
                                 created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                 updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                   )
         messages.success(request, "Data Added Successfully" )
         
         return redirect('/permission_index/')
         
    mydata = Permission.objects.all().values()
    context = {'permission': mydata}
    
    
    return render(request, 'permissions/index.html',context)

@login_required(login_url = "/user_login")
def permission_update(request, id):
    
    # return HttpResponse(id)
    
    Permission.objects.filter(id=id).update(permission = request.POST['permission'],
                                             edited_by=request.user.id,
                                             updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
 

    messages.success(request, 'Form submission successful')
    return redirect('/permission_index/')  
@login_required(login_url = "/user_login")
def permission_delete(request, id):
    
    # return HttpResponse(id)
    
    Permission.objects.filter(id=id).delete()
 

    messages.success(request, 'Form Deleted successful')
    return redirect('/permission_index/') 
    
#announcement
@login_required(login_url = "/user_login")
def announcement_index(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/index.html', {'announcements':announcements})

@login_required(login_url = "/user_login")
def announcement_create(request):
    now = datetime.now() 
    form = AnnouncementForm
    compact = {'form': form}
    if request.method == 'POST':  
         Announcement.objects.create(subject=request.POST['subject'],
                                     description=request.POST['description'],
                                     department=request.POST['department'],
                                     created_by=request.user.id,
                                     created_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                   )
         messages.success(request, "Data Added Successfully" )
         return redirect('/announcement_index/')
    return render(request, 'announcements/create.html', compact)

@login_required(login_url = "/user_login")
def announcement_show(request, id):
    announcements = Announcement.objects.get(id = id)
    form = AnnouncementForm(instance=announcements)
    compact = {'form': form, 'id':id, 'announcements':announcements }

    return render(request, 'announcements/show.html', compact)

@login_required(login_url = "/user_login")
def announcement_edit(request, id):
    announcements = Announcement.objects.get(id = id)
    now = datetime.now() 
    form = AnnouncementForm(instance=announcements)
    compact = {'form': form, 'id':id, 'announcements':announcements }
    if request.method == 'POST':  
         Announcement.objects.filter(id=id).update(subject=request.POST['subject'],
                                     description=request.POST['description'],
                                     department=request.POST['department'],
                                     edited_by=request.user.id,
                                     updated_at = now.strftime("%Y-%m-%d %H:%M:%S"),
                                   )
         messages.success(request, "Data Added Successfully" )
         return redirect('/announcement_index/')
    return render(request, 'announcements/edit.html', compact)

@login_required(login_url = "/user_login")
def announcement_delete(request, id):
    Announcement.objects.filter(id=id).delete()
    messages.success(request, 'Form Deleted successful')
    return redirect('/announcement_index/') 





