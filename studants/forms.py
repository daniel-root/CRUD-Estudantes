from django import forms
from .models import Studant
class StudantForm(forms.ModelForm):
    class Meta:
        model = Studant
        fields = '__all__'

        widgets = {
            'birth_date': forms.TextInput(attrs={'type': 'date'}),
            }
        