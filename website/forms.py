from django import forms

class yearSearch(forms.Form):
    videoname = forms.CharField(max_length=20,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'id':'inputName'
        }))

   
    