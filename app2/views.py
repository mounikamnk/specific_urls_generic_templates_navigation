from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse('virat content')

def virat2(request):
    return render(rquest,'virat.html')

