from django.forms import ModelForm, TextInput, URLInput, CheckboxInput, Select
from .models import Space

class AddSpaceForm(ModelForm):
    class Meta:
        model = Space
        fields = ["space_name", "is_type", "has_internet", "is_meeting_friendly", "url"]
        widgets = {
            'space_name': TextInput(attrs={
                'class': "input input-bordered input-primary w-full max-w-xs",
                'placeholder': 'Enter the name of the space'
            }),
            'is_type': Select(attrs={
                'class': "select select-bordered w-full max-w-xs", 
            }),
            'has_internet': CheckboxInput(attrs={
                'class': "checkbox checkbox-xs", 
            }),
            'is_meeting_friendly': CheckboxInput(attrs={
                'class': "checkbox checkbox-xs", 
            }),
            'url': URLInput(attrs={
                'class': "input input-bordered input-primary w-full max-w-xs",
                'placeholder':"Provide the map location of the space" 
            }),
        }
