from django.http import HttpResponse
from django.shortcuts import render

from home.forms import UserRegisterForm


# Create your views here.


def home(request):
    return HttpResponse("Hello, world. You're at the polls home view.")

def about(request, username):
    return HttpResponse("About You")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'register_done.html', {'user': user, 'form':form})

    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
