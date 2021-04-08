from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate

from .forms import CriarFormUser

def cadastro(request):
    context={}
    if request.POST:
        form = CriarFormUser(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password1='raw_password')
            login(request, user)
            return redirect('home')
        else :
            context['registration_form'] = form
    else:
        form = CriarFormUser()
        context['registration_form'] = form 
    return render(request, 'accounts/cadastro.html', context)