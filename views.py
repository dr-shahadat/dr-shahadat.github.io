#               {% static 'website/' %}


from django.shortcuts import render
from django.core.mail import send_mail


def func_homepage(request):
    return render(request, 'homepage.html', {})

def func_contact(request):
    if request.method == 'POST':
        var_customer_name = request.POST['name']
        var_customer_email = request.POST['email']
        var_customer_comments = request.POST['comments']

        send_mail(

        var_customer_name,                    # subject
        var_customer_comments,                # message
        var_customer_email,                   # from_email
        ['arique2104@gmail.com', 'juthi3174@gmail.com']            # to_mail

        )
        return render(request, 'contact.html', {'var_customer_name': var_customer_name})
    else:
        return render(request, 'contact.html', {})

def func_about(request):
    return render(request, 'about.html', {})

def func_treatment(request):
    return render(request, 'treatment.html', {})

def func_testimonials(request):
    return render(request, 'testimonials.html', {})

def func_gallery(request):
    return render(request, 'gallery.html', {})

def func_ourteam(request):
    return render(request, 'ourteam.html', {})

def func_appointment(request):
    if request.method == 'POST':
        var_patient_email = request.POST['q13_email13']
        var_patient_email = request.POST['q13_email13']
        var_patient_email = request.POST['q13_email13']


    return render(request, 'appointment.html', {})
















# python -m smtpd -n -c DebuggingServer localhost:1025
# 127.0.0.1:8000

# python3 manage.py makemigrations

# python3 manage.py migrate

# python3 manage.py runserver

# python3 manage.py createsuperuser

# python3 manage.py changepassword