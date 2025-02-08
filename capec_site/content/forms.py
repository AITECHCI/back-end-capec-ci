from django import forms
from .models import MyModel  # Remplacez par votre modèle

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'  # Utilisez tous les champs du modèle