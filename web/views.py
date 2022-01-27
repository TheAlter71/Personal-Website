from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        actual_message = 'Boss,\nSomeone make response to your personal website.\n\nName: ' + name + '\nEmail : ' + email + '\nSubject : ' + subject + '\nMessage :\n' + message 
        
        # SEND EMAIL
        send_mail(
            'Public Response!' , # Subject
            actual_message, # Message
            email , # From Email
            ['example@gmail.com'], # To Email
        )

        return HttpResponse('Thank you ' + name +  ', your message send successfully!')

    return render(request, 'index.html')
