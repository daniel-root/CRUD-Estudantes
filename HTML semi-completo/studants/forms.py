from django import forms
from .models import Studant
class StudantForm(forms.ModelForm):
    class Meta:
        model = Studant
        fields = '__all__'

        widgets = {
            'birth_date': forms.TextInput(attrs={'type': 'date'}),
            'cpf': forms.TextInput(attrs={'data-mask':"000.000.000-00",'data-mask-selectonfocus':"true"}),
            'phone': forms.TextInput(attrs={'data-mask':"(00) 0 0000-0000",'data-mask-selectonfocus':"true"})
            }
        