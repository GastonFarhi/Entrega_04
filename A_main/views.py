from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "A_main/index.html")


def about(request):
    return render(request, "A_main/about.html")
