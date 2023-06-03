from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('dhoni content')

def dhoni2(request):
    return render(request,'dhoni.html')
