from django import forms
from .models import Course, Comments


class CourseAddForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['slug', 'title', 'description', 'image']
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comment', 'author_com', 'lesson_com']
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'author_com': forms.HiddenInput(),
            'lesson_com': forms.HiddenInput(),
        }
