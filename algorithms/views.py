from django.shortcuts import render
from django.http import HttpResponse
from .forms import RomanForm
# Create your views here.
def roman(request):
    form = RomanForm()
    context = {
        'form': form,
    }

    number = 0
    context = {
        'value':value,
    }
    return render(request, 'algorithms/roman_number.html', {'context':context})
