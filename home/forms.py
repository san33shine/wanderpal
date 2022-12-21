from django import forms
from .models import story

class storyForm(forms.ModelForm):
    class Meta:
        model = story
        fields = ['story_title','story_desc','nickname','story_image','owner']
        widgets = {
            'story_desc': forms.Textarea(attrs={'rows': 3}),
        }
