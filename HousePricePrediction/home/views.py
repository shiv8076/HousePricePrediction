from django.shortcuts import render

from home.forms import formData
import pandas as pd
import pickle
model = pickle.load(open('./savedModel/pricePrediction.sav', 'rb'))
# Create your views here.


def index(request):
    if request.method == 'POST':
        c_form = formData(request.POST)
        if c_form.is_valid():
            predata = [[float(c_form.cleaned_data['crim']), float(c_form.cleaned_data['zn']), float(c_form.cleaned_data['indus']), float(c_form.cleaned_data['chas']), float(c_form.cleaned_data['nox']), float(c_form.cleaned_data['rm']), float(c_form.cleaned_data['age']), float(c_form.cleaned_data['dis']), float(c_form.cleaned_data['rad']), float(c_form.cleaned_data['tax']), float(c_form.cleaned_data['ptratio']), float(c_form.cleaned_data['b']), float(c_form.cleaned_data['lsat'])]]
            data = pd.DataFrame(predata)
            result = model.predict(data)
            content = {
                'result': str(result[0]),
                'forms': formData()
            }
            return render(request, 'ans.html', content)
        else:
            content = {
                'forms': formData()
            }
            return render(request, 'index.html', content)
    else:
        content = {
            'forms': formData()
        }
        return render(request, 'index.html', content)
