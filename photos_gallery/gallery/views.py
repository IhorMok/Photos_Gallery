import logging
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterUserForm

logger = logging.getLogger(__name__)


def index_page(request):
    return render(request, 'gallery/home.html')


def about(request):
    return render(request, 'gallery/about.html')


def register_page(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            logger.warning(form.errors)
    else:
        form = RegisterUserForm()

    return render(request, 'gallery/register_page.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'gallery/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('index')


def page_user(request):
    return render(request, 'gallery/page_user.html')
