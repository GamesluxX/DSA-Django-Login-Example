from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

User = get_user_model()

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    p = request.user
    u = p.username
    context = {
        'u': u
    }
    return render(request, 'home.html', context)
