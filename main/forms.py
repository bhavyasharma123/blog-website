from django import forms  # This was missing!
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'image_url', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Technical Title'}),
            'category': forms.Select(attrs={'class': 'form-select rounded-pill'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Paste high-res URL here'}),
            'content': forms.Textarea(attrs={'class': 'form-control rounded-4', 'rows': 10, 'placeholder': 'Write your engineering documentation here...'}),
            'status': forms.Select(attrs={'class': 'form-select rounded-pill'}),
        }