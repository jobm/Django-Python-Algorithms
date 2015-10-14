from django.shortcuts import render
from django.http import HttpResponse
from .forms import RomanForm
# Create your views here.
def roman(request):
    form = RomanForm(request.POST or None)
    value = 0
    context = {
        'form' : form
    }
    if form.is_valid():
        value = form.cleaned_data.get('roman_number')
        roman_value = convert_to_roman(value);
        context = {'form' : form, 'roman_value' : roman_value}
    return render(request, 'algorithms/roman_number.html', context)

def convert_to_roman(user_input):
     #create a dictionary of keys as the string roman and values as their respective data
     values = {"i":1, "v":5, "x":10, "l":50, "c":100, "m":1000}
     #sum the instance of each character found in user input based on the key, use a anonymous func
     if isinstance(user_input, str):
         return sum(map(lambda x: values[x], user_input))
     return 'v'
    #  print(convert_to_roman(get_user_input().lower()))
