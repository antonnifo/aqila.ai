import os

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .models import Contacts


def index(request):
    
    template = 'front_end/index.html'
    return render(request, template)

def contact(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        email      = request.POST['email']
        phone      = request.POST['phone']
        message    = request.POST['message']


        contact =Contacts(first_name=first_name, last_name=last_name, email=email,phone=phone,message=message)

        contact.save()

        # Send mail
        from_email_ = os.getenv('EMAIL_HOST_USER')
        send_mail(
            'INQUIRY ON OUR WEBSITE',
            f'There has been an inquiry by {first_name} login to the admin panel  for more info',
            f'{ from_email_ }',
            [os.getenv('RECIPIENT_1'), os.getenv('RECIPIENT_2'),os.getenv('RECIPIENT_3'),os.getenv('RECIPIENT_4')],
            fail_silently=False

        )

        messages.success(request, "Your message has been submitted we will get back to you asap")

        return redirect('index')   

    else:
        return redirect('index')  
