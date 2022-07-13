import logging
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
            return redirect('index')
        else:
            logger.warning(form.errors)
    else:
        form = RegisterUserForm()

    return render(request, 'gallery/register_page.html', {'form': form})
