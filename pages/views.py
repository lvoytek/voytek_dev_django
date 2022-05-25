from django.shortcuts import render

context = {
    'mobile': False
}


def index(request):
    return render(request, 'index.html', context=context)


def resume(request):
    return render(request, 'resume.html', context=context)