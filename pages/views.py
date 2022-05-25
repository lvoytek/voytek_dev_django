from django.shortcuts import render

context = {
    'mobile': False
}


def index(request):
    return render(request, 'index.html', context=context)
