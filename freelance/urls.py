from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard),
    path('master/', views.master),
    path('masterpage/', views.masterpage),

    path('user_login/', views.user_login),
    path('user_register/', views.user_register),
    path('user_logout/', views.user_logout),

    # Payment Type Starts
    path('paytypeindex/',views.paytypeindex),
    path('pay_update/<id>',views.pay_update),
    path('pay_delete/<id>',views.pay_delete),
    # Payment Type Ends


    # Payment Mode Starts
    path('paymodeindex/',views.paymodeindex),
    path('paymode_update/<id>',views.paymode_update),
    path('paymode_delete/<id>',views.paymode_delete),
    # Payment Mode Ends

    # Payment To Bank Starts
    path('paybank_delete/<id>',views.paybank_delete),
    path('paybank_update/<id>',views.paybank_update),
    path('payindex/',views.payindex),
    # Payment To Bank Ends


    # Company Starts
    path('company_index/', views.company_index),
    path('company_create/', views.company_create),
    path('company_edit/<int:id>', views.company_edit),
    path('company_delete/<int:id>', views.company_delete),
    # Company Ends

    # Currency Starts
    path('currency_index/', views.currency_index),
    path('currency_create/', views.currency_create),
    path('currency_edit/<int:id>', views.currency_edit),
    path('currency_delete/<int:id>', views.currency_delete),
    # Currency Ends


    # Month Starts
    path('month_index/', views.month_index),
    path('month_create/', views.month_create),
    path('month_edit/<int:id>', views.month_edit),
    path('month_delete/<int:id>', views.month_delete),
    # Month Ends

    # Job Details Starts
    path('jobindex/',views.jobindex),
    path('job_update/<id>',views.job_update),
    path('job_delete/<id>',views.job_delete),
    path('job_report/',views.job_report),
    path('job_report_search/',views.job_report_search),
    # Jon Detail Ends

    # CRM Starts
    path('crm_index/',views.crm_index_form),
    path('crm_edit/<id>',views.crm_edit),
    path('crm_delete/<id>',views.crm_delete),
    # CRM Ends

    # Country Starts 

    path('countries/',views.country_index),
    path('country_delete/<id>',views.country_delete),
    path('country_show/<id>',views.country_show),
    path('country_edit/<id>',views.country_edit),
    # Country Ends















    



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)