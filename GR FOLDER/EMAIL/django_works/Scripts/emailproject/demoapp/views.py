from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
# how to send common smtp email using Django and settings required for sending email in settings.
def sendanemail(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        #print(to,content)
        send_mail(
            #subject
            "testing",
            #message
            content,
            #from mail
            settings.EMAIL_HOST_USER,
            #rec list
            [to]
        )
        return render(request, 'demoapp/email.html',
                      {
                          'title': 'send an email'
                      }
                     )
    else:
        return render(request,'demoapp/email.html',
                      {
                          'title':'send an email'
                      }
                     )