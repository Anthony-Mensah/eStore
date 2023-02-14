from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth.models import auth
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .token import account_activation_token
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.error(request, "{} has been taken".format(email))
                return redirect('user:register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, "{} has been taken".format(username))
                return redirect('user:register')
            else:
                user = User.objects.create_user(
                username=username,
                email=email,
                )
                user.set_password(password)
                user.save()
                #send email to user
                current_site = get_current_site(request)
                subject = "Verify your email"
                message = render_to_string('user/account_activate.html', {
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
                })
                user.email_user(subject, message)
                return render(request, 'user/email_alert.html')


        else:
            messages.error(request, "Password do not match")
            return redirect('user:register')

    return render(request, 'user/register.html')

def activate_user(request, uidb64, token):
    try:
        user_id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=user_id)
    except():
        print("ERROR WITH uidb64")

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('/')
    else:
        return render(request, 'user/account_activation_invalid.html')

def login(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Email or Password doesn't match")

    return render(request, 'user/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def check_email(request):
    return render(request, 'user/check_email.html')
