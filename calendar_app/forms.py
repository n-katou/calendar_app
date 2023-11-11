from django import forms
from .models import TodoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'memo','priority', 'start_date','end_date']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }