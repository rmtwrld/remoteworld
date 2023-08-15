from django.forms import ModelForm
from .models import Space

class AddSpaceForm(ModelForm):
    class Meta:
        model = Space
        fields = ["space_name", "is_type", "has_internet", "is_meeting_friendly", "url"]
