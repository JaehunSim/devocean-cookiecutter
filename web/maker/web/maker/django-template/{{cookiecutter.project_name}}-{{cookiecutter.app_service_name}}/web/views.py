from django.shortcuts import render


def index(request):
    context = {'value': 'apple'}
    response = render(request, 'web/index.html', context)
    return response
