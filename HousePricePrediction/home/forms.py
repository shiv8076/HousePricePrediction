from cProfile import label
from django import forms

class formData(forms.Form):
    crim = forms.DecimalField()
    zn = forms.DecimalField()
    indus = forms.DecimalField()
    chas = forms.DecimalField()
    nox = forms.DecimalField()
    rm = forms.DecimalField()
    age = forms.DecimalField()
    dis = forms.DecimalField()
    rad = forms.DecimalField()
    tax = forms.DecimalField()
    ptratio = forms.DecimalField()
    b = forms.DecimalField()
    lsat = forms.DecimalField()