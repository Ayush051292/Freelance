from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('form_index/', views.form_index),
    path('form_edit/<int:id>',views.form_edit),
    path('form_delete/<int:id>',views.form_delete),
    path('shift_index/', views.shift_index),
    path('getshift/',views.getshift, name='getshift'),
    path('demo_form_index/', views.demo_form_index),
    path('user_form_index/', views.user_form_index),
    path('user_form_show/', views.user_form_show),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)