from django.shortcuts import render


def index_page(request):
    return render(request, 'gallery/home.html')


def about(request):
    return render(request, 'gallery/about.html')
