from django.db import models

import datetime

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User



# Create your models here.

class Paymenttype(models.Model):
    payment_type = models.CharField(max_length=255)
    payroll = models.CharField(max_length=255,null=True)
    bank = models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=255,null=True)
    created_at = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=255)

class Paymentmode(models.Model):
    payment_mode = models.CharField(max_length=255)
    p_order = models.CharField(max_length=255,null=True)
    max_allocation = models.CharField(max_length=255,null=True)
    display_name = models.CharField(max_length=255,null=True)
    created_at = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=255)


class Companies(models.Model):
    payroll = models.CharField(max_length=255)
    pandeduct = models.CharField(max_length=255)
    tandeduct = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    gstn = models.CharField(max_length=255)
    max_emp = models.CharField(max_length=255,null=True)
    max_crm = models.CharField(max_length=255,null=True)
    clogo = models.FileField(upload_to="Files",null=True)
    email = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=255,null=True)
    regno = models.CharField(max_length=255,null=True)
    trade_license = models.CharField(max_length=255,null=True)
    created_at = models.CharField(max_length=255, null=True)
    updated_at = models.CharField(max_length=255, null=True)


class Month(models.Model):
    month = models.CharField(max_length=255)
    created_at = models.CharField(max_length=255, null=True)
    updated_at = models.CharField(max_length=255, null=True)

class Currencies(models.Model):
    currency = models.CharField(max_length=255)
    rate = models.CharField(max_length=255)
    created_at = models.CharField(max_length=255, null=True)
    updated_at = models.CharField(max_length=255, null=True)

class Paymentobank(models.Model):
    payment_to_bank = models.CharField(max_length=255)
    payroll = models.ForeignKey(Companies ,on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=255,null=True)
    account_no = models.CharField(max_length=255,null=True)
    branch = models.CharField(max_length=255,null=True)
    pan = models.CharField(max_length=255,null=True)   
    ifsc = models.CharField(max_length=255,null=True)
    swift_code = models.CharField(max_length=255,null=True) 
    created_at = models.DateTimeField(max_length=255)
    updated_at = models.DateTimeField(max_length=255)

class Jobdetail(models.Model):
    crm = models.CharField(max_length=255,null=True)
    job_id = models.CharField(max_length=255,null=True)
    words = models.IntegerField(null=True)
    value = models.IntegerField(null=True)
    ppw = models.DecimalField(decimal_places=2,max_digits=4, blank=True,null=True)
    currency = models.CharField(max_length=255,null=True)
    value_inr = models.IntegerField(null=True)
    participant = models.CharField(max_length=255,null=True)
    created_by = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(max_length=255,null=True)
    updated_at = models.DateTimeField(max_length=255,null=True)

class Country(models.Model):
    country_name=models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(max_length=255,null=True)
    updated_at = models.DateTimeField(max_length=255,null=True)


class Crm(models.Model):
    crm_name=models.CharField(max_length=100, null=True)
    crm_number=models.CharField(max_length=100, null=True)
    payment_type=models.ForeignKey(Paymenttype ,on_delete=models.CASCADE)
    payment_mode=models.ForeignKey(Paymentmode ,on_delete=models.CASCADE)
    per_word_rate_mother=models.CharField(max_length=100, null=True)
    per_word_rate_inr=models.CharField(max_length=100, null=True)
    currency=models.ForeignKey(Currencies ,on_delete=models.CASCADE)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE)
    bank=models.ForeignKey(Paymentobank ,on_delete=models.CASCADE)
    credit_limit=models.CharField(max_length=100, null=True)
    gst=models.CharField(max_length=100, null=True)
    tds=models.CharField(max_length=100, null=True)
    inv_email=models.CharField(max_length=100, null=True)
    contact_email=models.CharField(max_length=100, null=True)
    mobile=models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(max_length=255,null=True)
    updated_at = models.DateTimeField(max_length=255,null=True)
    created_by = models.CharField(max_length=255,null=True)

class Emplevel(models.Model):
    created_by = models.CharField(max_length=255)
    level = models.CharField(max_length=255,null=True)
    type = models.CharField(max_length=255,null=True)
    max_word = models.CharField(max_length=255,null=True)
    min_word = models.CharField(max_length=255,null=True)
    monthly_max_word = models.CharField(max_length=255,null=True)
    monthly_min_word = models.CharField(max_length=255,null=True)
    ppw = models.DecimalField(decimal_places=2,max_digits=4, blank=True,null=True)
    edited_by = models.CharField(max_length=255,null=True)
    year = models.CharField(max_length=255,null=True)
    month = models.CharField(max_length=255,null=True)
    date = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(max_length=255,null=True)
    updated_at = models.DateTimeField(max_length=255,null=True)
    
    
class Custlevel(models.Model):
    created_by = models.CharField(max_length=255)
    level = models.CharField(max_length=255,null=True)
    type = models.CharField(max_length=255,null=True)
    max_word = models.CharField(max_length=255,null=True)
    min_word = models.CharField(max_length=255,null=True)
    monthly_max_word = models.CharField(max_length=255,null=True)
    monthly_min_word = models.CharField(max_length=255,null=True)
    ppw = models.DecimalField(decimal_places=2,max_digits=4, blank=True,null=True)
    edited_by = models.CharField(max_length=255,null=True)
    year = models.CharField(max_length=255,null=True)
    month = models.CharField(max_length=255,null=True)
    date = models.CharField(max_length=255,null=True)
    created_at = models.CharField(max_length=255,null=True)
    updated_at = models.CharField(max_length=255,null=True)

class Teammaster(models.Model):
    team = models.CharField(max_length=255, null=True)
    # type = models.CharField(max_length=255, null=True)
    f_strategy = models.CharField(max_length=255, null=True)
    m_strategy = models.CharField(max_length=255, null=True)
    comp1 = models.CharField(max_length=255, null=True)
    comp2 = models.CharField(max_length=255, null=True)
    comp3 = models.CharField(max_length=255, null=True)
    created_at = models.CharField(max_length=255,null=True)
    updated_at = models.CharField(max_length=255,null=True)
    status = models.CharField(default='1',max_length=255)
    created_by = models.CharField(max_length=255,null=True)
    edited_by = models.CharField(max_length=255,null=True)



class Cmfmaster(models.Model):
    name = models.CharField(max_length=255,null=True)
    type = models.CharField(max_length=255,null=True)
    status = models.CharField(default='1', max_length=255)
    created_at = models.CharField(max_length=255,null=True)
    updated_at = models.CharField(max_length=255,null=True)
    created_by = models.CharField(max_length=255,null=True)
    updated_by = models.CharField(max_length=255,null=True)
    
class Strategymaster(models.Model):
    strategy = models.CharField(max_length=255,null=True)
    t1 = models.CharField(max_length=255,null=True)
    t2 = models.CharField(max_length=255,null=True)
    t3 = models.CharField(max_length=255,null=True)
    t4 = models.CharField(max_length=255,null=True)
    status = models.CharField(default='1', max_length=255)
    created_at = models.CharField(max_length=255,null=True)
    updated_at = models.CharField(max_length=255,null=True)
    created_by = models.CharField(max_length=255,null=True)
    updated_by = models.CharField(max_length=255,null=True)    
    
class Marketingstrategy(models.Model):
    type = models.CharField(max_length=255,null=True)
    value = models.CharField(max_length=255,null=True)
    created_at = models.CharField(max_length=255,null=True)
    updated_at = models.CharField(max_length=255,null=True)
    created_by = models.CharField(max_length=255,null=True)
    updated_by = models.CharField(max_length=255,null=True)

class Termcondition(models.Model):
    subject = models.CharField(max_length=255,null=True)
    type = models.CharField(max_length=255,null=True)
    content = RichTextField()
    status = models.CharField(default='1',max_length=255)
    created_by = models.CharField(max_length=255, null=True)
    created_at = models.CharField(max_length=255, null=True)
    updated_at = models.CharField(max_length=255, null=True)

class Location(models.Model):
    location=models.CharField(max_length=255)
    created_at = models.CharField(max_length=255, null=True)
    updated_at = models.CharField(max_length=255, null=True)
    created_by=models.CharField(max_length=255,null=True)

class Designation(models.Model):
    designation=models.CharField(max_length=255)
    created_at = models.CharField(max_length=255, null=True)
    updated_at = models.CharField(max_length=255, null=True)
    created_by = models.CharField(max_length=255,null=True)

class Role(models.Model):
    name = models.CharField(max_length=255,null=True)
    created_by = models.CharField(max_length=255,null=True)
    edited_by = models.CharField(max_length=255,null=True)
    created_at = models.CharField(max_length=255, null=True)
    updated_at = models.CharField(max_length=255, null=True)

class Permission(models.Model):
    permission=models.CharField(max_length=255,null=True)
    created_by=models.CharField(max_length=255,null=True)
    edited_by=models.CharField(max_length=255,null=True)
    created_at = models.CharField(max_length=255, null=True)
    updated_at = models.CharField(max_length=255, null=True)
    
class Announcement(models.Model):
    subject = models.CharField(max_length=255,null=True)
    description = RichTextUploadingField()
    department = models.CharField(max_length=255,null=True)
    status = models.CharField(default='1', max_length=255)
    created_by = models.CharField(max_length=255,null=True)
    edited_by = models.CharField(max_length=255,null=True)
    created_at = models.CharField(max_length=255, null=True)
    updated_at = models.CharField(max_length=255, null=True)


class Freelancer(models.Model):
    #register
    name=models.CharField(max_length=255, default='')
    email=models.EmailField(default='')
    pan=models.CharField(max_length=20, default='')
    
    #personal
    image=models.FileField(upload_to="Files",default='')
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    phone=models.CharField(max_length=20,null=True)
    doj=models.CharField(max_length=255,null=True)
    dob=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=255,null=True)
    blood=models.CharField(max_length=20,null=True)
    aadhar=models.CharField(max_length=20,null=True)
    # pan=models.CharField(max_length=20, default='')

    #academic
    school=models.CharField(max_length=255, null=True)
    degree=models.CharField(max_length=255, null=True)
    subject=models.CharField(max_length=255, null=True)
    university=models.CharField(max_length=255, null=True)
    marks=models.CharField(max_length=255,null=True)

    # bank
    ifsc=models.CharField(max_length=255, null=True)
    accno=models.CharField(max_length=255, null=True)
    bank=models.CharField(max_length=255, null=True)

    #system
    user_id=models.CharField(max_length=255, null=True)
    user_type=models.CharField(max_length=255, default='')
    auth_user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='auth_user')
    reported_to=models.ForeignKey(User,on_delete=models.CASCADE, related_name='reported_to')
    role=models.ForeignKey(Role,on_delete=models.CASCADE,)
    department=models.ForeignKey(Companies,on_delete=models.CASCADE)
    designation=models.ForeignKey(Designation,on_delete=models.CASCADE)
    status=models.CharField(max_length=10, null=True)
    salary=models.CharField(max_length=255,null=True)
    init_level=models.CharField(max_length=255, default='')
    curr_level=models.CharField(max_length=255, default='')
    created_at = models.CharField(max_length=255, null=True)
    updated_at = models.CharField(max_length=255, null=True)
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='updated_by')

    