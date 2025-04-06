from django import forms
from .models import Post
from .models import Question

class Postform(forms.ModelForm):
  class Meta:
    model=Post
    fields=['title','content']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']