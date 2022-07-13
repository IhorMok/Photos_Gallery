from django.shortcuts import render, redirect
from .forms import RegisterUserForm


def index_page(request):
    return render(request, 'gallery/home.html')


def about(request):
    return render(request, 'gallery/about.html')


def register_page(request):
    # error = ''
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        # else:
        #     error = 'The form was not valid !!'
    else:
        form = RegisterUserForm()

    return render(request, 'gallery/register_page.html', {'form': form})
