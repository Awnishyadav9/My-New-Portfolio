from django.shortcuts import render, redirect
from .forms import Userform
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages

def first(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            instance = form.save()
            name = instance.name
            user_mail = instance.user_email
            content = instance.user_query

            html = render_to_string('emails/contact_form_email.html', {
                'name': name,
                'email': user_mail,
                'content': content
            })
            
            try:
                send_mail(
                    'The contact form subject',
                    'This is the message',
                    'noreply@awy8543.com',
                    ['awy8543@gmail.com'],
                    html_message=html
                )
                messages.success(request, "Your query has been sent successfully!")
            except Exception as e:
                messages.error(request, f"Failed to send your query: {e}")

            return redirect('/#form_section')
    else:
        form = Userform()
    
    return render(request, 'portfolio_template/index.html', {'user_form': form})
