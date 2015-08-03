from django.shortcuts import render, HttpResponse
from forms import RomanNumeralForm
from collections import OrderedDict

roman_dict = {
    'M': 1000,
    'CM': 900,
    'D':  500,
    'CD': 400,
    'C':  100,
    'XC': 90,
    'L':  50,
    'XL': 40,
    'X':  10,
    'IX': 9,
    'V':  5,
    'IV': 4,
    'I':  1
}
roman_dict = OrderedDict(sorted(roman_dict.items(), key=lambda t: -t[1]))

def int2numeral(integer):
    """Convert a base-10 integer into a roman numeral."""
    integer = int(integer)
    assert integer > 0, "Number must be greater than 0"
    assert integer < 3999, "Number must be less than 3999"
    representation = ""
    for entry in roman_dict.items():
        letter, i = entry
        while integer >= i:
            representation += letter
            integer -= i
    return representation

def home(request):
    context = dict()
    if request.method == "POST":
        form = RomanNumeralForm(request.POST)
        if form.is_valid():
            c = form.cleaned_data
            context['roman_numeral'] = (c['number'], int2numeral(c['number']))
    else:
        form = RomanNumeralForm()
    return render(request, "home.html", context)


