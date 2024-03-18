from django.contrib import admin
from django.urls import path, include
from email_management import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('add_email/', views.add_email, name='add_email'),
    path('send_emails/', views.send_emails, name='send_emails'),
    path('sms_form/', views.send_sms, name='sms_form'),
    path('success_addedmail/', views.success_addedmail, name='success_addedmail'),
    path('sent_email_success', views.sent_email_success, name='sent_email_success'),
   
    
    path('admin/', admin.site.urls), 
]