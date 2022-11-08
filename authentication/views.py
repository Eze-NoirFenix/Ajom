from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib import messages



def UserSignup(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            htmly = get_template('signup/signup_email.html')
            d = { 'username': username }
            subject, from_email, to = 'Bienvenido/a', 'theezelnar.arg@outlook.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'Bienvenido/a')

            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'signup/signup.html', {'form': form, 'title':'Sign up'})

def UserLogout(request):

    logout(request)

    return redirect('home')

def UserLogin(request):
    if request.method == 'POST':
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user is not None:

            form = login(request, user)
            return redirect('home')

        else:

            messages.info(request, f'Por favor inicie sesión con su usuario')

    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form':form, 'title':'log in'})

def UserEdit(request):

    form = UserChangeForm
    return render(request, 'edit_profile/edit_profile.html', {'form':form})

