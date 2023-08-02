from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('test_index/', views.test_index),
    path('test_index1/', views.test_index1),
    path('test_form/', views.test_form),
    path('form_index/', views.form_index),
    path('form_edit/<int:id>',views.form_edit),
    path('form_delete/<int:id>',views.form_delete),
    path('form_download_file/<int:id>',views.form_download_file)

]