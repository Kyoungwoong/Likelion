from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request, 'index.html')

def second(request):
    return render(request , 'second.html')