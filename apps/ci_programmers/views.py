from django.shortcuts import render


def index(request):
    template = 'ci_programmers/index.html'
    context = {}

    return render(request, template, context)
