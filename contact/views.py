from django.shortcuts import render, redirect

from .forms import ContactForms

from django.core.mail import EmailMessage

def contact(request):

    contact_forms = ContactForms()

    if request.method == 'POST':
        contact_forms = ContactForms(data=request.POST)

        if contact_forms.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')

            email = EmailMessage('Mensaje desde A Jurney of Mine',
            'Usuario: {}\nCorreo: {}\n\n{}'.format(name, email, content),
             'theezelnar.arg@outlook.com', ['theezelinar.arg@gmail.com'], reply_to=[email])

            try:
                email.send()

                return redirect('/contacto/?valido')

            except:

                return redirect('/contacto/?error')

    return render(request, 'contact/contact.html', {'contactme':contact_forms})
