from django.shortcuts import render

# Create your views here.
def boards(request):
    return render(request, 'board.html')

def boardfirst(request):
    return render(request , 'boardfirst.html')