from django import forms


class RomanNumeralForm(forms.Form):
    number = forms.IntegerField(
        label="Enter a number between 1 and 3999",
        min_value=1, max_value=3999
    )   
