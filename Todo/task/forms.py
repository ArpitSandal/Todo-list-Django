from django import forms

from .models import *

class TodoForm(forms.ModelForm):
    
    title      = forms.CharField(widget=forms.TextInput(
                    attrs={
                        "placeholder": "Your Title",
                        }
                    )
                )
    description     = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Add a description for your task",
            }
        ),
    )

    completed   = forms.BooleanField(label='', required=False)
    
    class Meta:
        model = Todo
        fields = [
            'title',
            'description',
            'completed'
        ]
