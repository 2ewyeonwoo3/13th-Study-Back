from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from community.models import *

# Create your views here.

def list(request):
    posts = Post.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post':post})

def question_list(request):
    questions = Question.objects.only('title', 'upload_time', 'name', 'status').order_by('upload_time')
    return render(request, 'question_list.html', {'questions':questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'question_detail.html', {'question':question})