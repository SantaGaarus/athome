from django.shortcuts import render


def homepage(request):
    return render(request, 'mainpage/home.html')
def korzina(request):
    return render(request, 'mainpage/korz.html')