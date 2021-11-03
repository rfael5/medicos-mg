from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ('num', 'nome', 'status', 'especializacao')
