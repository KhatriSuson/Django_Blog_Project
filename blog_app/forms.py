from django import forms
from django_summernote.widgets import SummernoteWidget

from blog_app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the title of post",
                }
            ),
            "content": SummernoteWidget(),
        }


    # summernote widgets in forms.py
        
