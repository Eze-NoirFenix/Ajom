from django.shortcuts import render

def home(request):

    return render(request, 'proyecto_web_app/home.html')

def privacy_policy(request):

    return render(request, 'legal/privacy_policy.html')

def cookies_policy(request):

    return render(request, 'legal/cookies_policy.html')

def aboutme(request):

    return render(request, 'aboutme/aboutme.html')
