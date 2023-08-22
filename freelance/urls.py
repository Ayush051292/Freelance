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

 #emplevel Starts
 
    
    path('emplevelindex/',views.emplevelindex),
    path('level_delete/<id>',views.level_delete),
    path('level_update/<id>',views.level_update),
 

 #emplevel Ends


# Cust level Starts
    path('custlevelindex/',views.custlevelindex),
    path('custlevel_delete/<id>',views.custlevel_delete),
    path('custlevel_update/<id>',views.custlevel_update),
#Cust Level Ends

  # Team Master Starts
    path('teammaster/',views.teammaster),
    path('teammaster_edit/<id>',views.teammaster_edit),
    path('teammaster_delete/<id>',views.teammaster_delete),
    # Team Master Ends
    
    #team+company ajax
    path('team_company/<id>',views.team_company),
    path('team_company2/<id>/<id1>',views.team_company2),
    path('team_company11/<id>',views.team_company11),
    path('team_company22/<id>/<id1>',views.team_company22),


    # CMF Master Starts
    path('cmfmaster/',views.cmfmasterindex),
    path('cmfmaster_delete/<id>',views.cmfmaster_delete),
    path('cmfmaster_update/<id>',views.cmfmaster_update),
    # CMF Master Ends

    # strategy Master Starts
    path('strategymaster/',views.strategymasterindex),
    path('strategymaster_delete/<id>',views.strategymaster_delete),
    path('strategymaster_update/<id>',views.strategymaster_update),
    # strategy Master Ends
    
    # marketing strategy Master Starts
    path('marketingstrategy/',views.marketingstrategyindex),
    path('marketingstrategy_delete/<id>',views.marketingstrategy_delete),
    path('marketingstrategy_update/<id>',views.marketingstrategy_update),
    # marketing strategy Master Ends
    
    
    # Terms & Conditions Starts 
    path('termcondition_index/',views.termcondition_index),
    path('termcondition_create/',views.termcondition_create),
    path('termcondition_edit/<id>',views.termcondition_edit),
    path('termcondition_show/<id>',views.termcondition_show),
    path('termcondition_update/<id>',views.termcondition_update),
    path('termcondition_delete/<id>',views.termcondition_delete),
    # Terms & Conditions Ends 
    
    # Location Starts 
    path("locations/",views.location_index),
    path("location_delete/<id>",views.location_delete),
    path("location_edit/<id>",views.location_edit),
    # Location Ends

    
    # Designation Starts 
    path("designations/",views.designation_index),
    path("designation_delete/<id>",views.designation_delete),
    path("designation_edit/<id>",views.designation_edit),
    # Designation Ends
    
    
    # Role Starts
    path('role_index/',views.role_index),
    path('role_delete/<id>',views.role_delete),
    path('role_update/<id>',views.role_update),
    #Role Ends

    # Permission Starts
    path('permission_index/',views.permission_index),
    path('permission_update/<id>',views.permission_update),
    path('permission_delete/<id>',views.permission_delete),
    #Permisssion Ends
    
    

    # announcement
    path('announcement_index/',views.announcement_index),
    path('announcement_create/',views.announcement_create),
    path('announcement_show/<id>',views.announcement_show),
    path('announcement_edit/<id>',views.announcement_edit),
    path('announcement_delete/<id>',views.announcement_delete),
    
    #Profile
    path('user_profile/', views.user_profile),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)