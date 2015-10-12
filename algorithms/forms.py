from django import forms

class RomanForm(forms.Form):
    roman_number = forms.CharField(label="Enter Roman Number",min_length=1,max_length=10)
    # output_number = forms.IntegerField()
