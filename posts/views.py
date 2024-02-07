from django.shortcuts import render



# for test template only
def index(request):
    return render(request, 'index.html')