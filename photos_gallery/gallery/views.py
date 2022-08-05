import logging
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterUserForm, AlbumForm

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
            return redirect('page_user')
        else:
            return redirect('login')
    else:
        return render(request, 'gallery/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('index')


def page_user(request):
    return render(request, 'gallery/page_user.html')


def create_album(request):
    if request.method == "POST":
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album = album_form.save(commit=False)
            album.user = request.user
            album.save()
            return redirect('index')
    else:
        album_form = AlbumForm()

    logger.warning(album_form.errors)
    return render(request, 'gallery/create_album.html', {'album_form': album_form})
