from django import forms
from .models import Challenge

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['book', 'title','description','completed']
        labels = {
            'book': 'Obra',
            'title': 'Objetivo',
            'description': 'Desafio',
        }
class ChallengeFormUpdate(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['book', 'title','description']
        labels = {
            'book': 'Obra',
            'title': 'Objetivo',
            'description': 'Desafio',
        }