from django import forms

from .models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('name', 'email', 'contact', 'college', 'university_roll', 'certificate')
        labels = {
            'name': ('Name'),
            'email': ('Email'),
            'contact': ('Phone'),
            'college': ('College'),
            'university_roll': ('University Roll No.:'),
            'certificate': ('Certificate')
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'required': 'required'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'college': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'university_roll': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'certificate': forms.Select(
                choices=[
                    (1, 'Kriraathon \'19 Participation - Sports - 5 Pts.'),
                    (2, 'How To Not Be Average? - GD - 10 Pts.'),
                    (3, 'From Thermometer To Thermostat - GD - 10 Pts.')
                ], attrs={'class': 'form-control', 'required': 'required'})
        }
    #email = forms.EmailField(required=True, label='Email Address')
    #contact = forms.CharField(max_length=15, required=True, label='Phone')
    #college = forms.CharField(max_length=15, required=True, label='College')
    #university_roll = forms.CharField(max_length=15, required=True, label='University Roll No.:')
    #certificate = forms.ChoiceField(choices=[(1, 'Kriraathon Certificate'), (2, 'Rotaract Certificate')])