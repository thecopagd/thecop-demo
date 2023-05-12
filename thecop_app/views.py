from django.shortcuts import render


def index(request):
    return render(request, 'thecop_app/index.html')

