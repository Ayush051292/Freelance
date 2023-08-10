from django.db import models

# Create your models here.

class Paymenttype(models.Model):
    payment_type = models.CharField(max_length=255)
    payroll = models.CharField(max_length=255,null=True)
    bank = models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(max_length=255)
    updated_at = models.DateTimeField(max_length=255)

class Paymentmode(models.Model):
    payment_mode = models.CharField(max_length=255)
    p_order = models.CharField(max_length=255,null=True)
    max_allocation = models.CharField(max_length=255,null=True)
    display_name = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(max_length=255)
    updated_at = models.DateTimeField(max_length=255)


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
    payroll = models.CharField(max_length=255,null=True)
    bank_name = models.CharField(max_length=255,null=True)
    account_no = models.CharField(max_length=255,null=True)
    branch = models.CharField(max_length=255,null=True)
    pan = models.CharField(max_length=255,null=True)   
    ifsc = models.CharField(max_length=255,null=True)   
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






    