from django import forms
from pratyakshapp.models import jobmodel, uploadmodel,advertisemodel,contactmodel

class jobFor(forms.ModelFarm):
    class Meta:
        model = jobmodel
        fields = '__all__'

    
class uploadForm(forms.ModelFarm):
    class Meta:
        model = uploadmodel
        fields = '__all__'


class advertiseForm(forms.ModelFarm):
    class Meta:
        model = advertisemodel
        fields = '__all__'       


class contacts(forms.ModelFarm):
    class Meta:
        model =contactmodel
        fields = '__all__'      