from django import forms
from .models import Post, Question, Comment 

class Postform(forms.ModelForm):
  class Meta:
    model=Post
    fields=['title','content','photo']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content','photo']

class Commentform(forms.ModelForm):
   class Meta:
      model=Comment
      fields=['username','comment_text']