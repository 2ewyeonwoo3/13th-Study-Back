from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from community.models import Post
from community.models import Question
# Create your views here.

def List(request):
  posts = Post.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
  questions = Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
  return render(request, 'list.html', {'posts':posts, 'questions': questions,})

def detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'detail.html', {'post':post})

def question_detail(request, pk):
  question = get_object_or_404(Question, pk=pk)
  return render(request, 'question_detail.html', {'question': question})

# 각각 따로 만들고 싶다면 함수를 따로 분리해서 만들기!, html도 분리