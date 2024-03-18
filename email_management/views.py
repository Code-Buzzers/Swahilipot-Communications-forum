from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from .models import UserProfile
from django.db import IntegrityError
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from twilio.rest import Client
from .forms import SMSSendForm

def home(request):
    return render(request, 'home.html')

def success_addedmail(request):
    return render(request, 'success_addedmail.html')

def sent_email_success(request):
    return render(request, 'sent_email_success.html')

def add_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            UserProfile.objects.create(email=email)
            
            # Send email with default message
            subject = settings.DEFAULT_EMAIL_SUBJECT
            body = settings.DEFAULT_EMAIL_BODY
            send_mail(subject, body, settings.EMAIL_HOST_USER, [email])
            
            return redirect('success_addedmail')
        except IntegrityError:
            return HttpResponse("Email already exists")
    return render(request, 'add_email.html')

def send_emails(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        recipients = UserProfile.objects.values_list('email', flat=True)
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipients, fail_silently=False)
        return redirect('sent_email_success')
    return render(request, 'send_emails.html')


def send_sms(request):
    if request.method == 'POST':
        form = SMSSendForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            recipients = form.cleaned_data['recipients'].split(',')
            # Send SMS using Twilio
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            for recipient in recipients:
                message = client.messages.create(
                    body=message,
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to=recipient.strip()
                )
            return render(request, 'success.html')
    else:
        form = SMSSendForm()
    return render(request, 'sms_form.html', {'form': form})
