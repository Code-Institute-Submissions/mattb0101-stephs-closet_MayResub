from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages
from .forms import EmailForm


def index(request):
    """ View to create index page return """
    return render(request, 'home/index.html')


def email(request):
    """ view to take to email page to email questions to the store """
    form = EmailForm

    if request.method == 'POST':
        email = form(data=request.POST)

        if email.is_valid():
            contact_name = request.POST.get('contact_name', '')
            message = request.POST.get('message', '')
            contact_email = request.POST.get('contact_email', '')

            template = get_template('home/emails/contact_temp.txt')
            context = {
                'contact_name': contact_name,
                'message': message,
                'contact_email': contact_email,
            }
            content = template.render(context)

            email = EmailMessage(
                "New Things",
                content,
                "Stephs Closet" + '',
                ['stephsclosetstore@gmail.com'],
                headers={'Reply to': contact_email}
            )
            email.send()
            messages.success(request, 'Thanks very much for messaging us! \
                We will get back to you as soon as we can!')
            return redirect('email')

    context = {
        'form': form,
    }

    return render(request, 'home/email.html', context)
