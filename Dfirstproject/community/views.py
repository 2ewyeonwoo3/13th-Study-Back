from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from community.models import Post
from community.models import Question
from community.forms import Postform
from community.forms import QuestionForm

# Create your views here.

def List(request):
  posts= Post.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
  questions= Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
  return render(request, 'list.html', {'posts':posts, 'questions':questions})

def detail (request,pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'detail.html', {'post':post})

def question_List(request):
  questions= Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
  return render(request, 'question_list.html', {'questions':questions})

def question_detail(request, pk):
    questions = get_object_or_404(Question, pk=pk)
    return render(request, 'question_detail.html', {'question': questions})


def new(request):
   form=Postform() #form이라는 이름으로 폼 객체 선언
   return render(request, 'new.html',{'form':form})
  

def create(request):
   form = Postform(request.POST, request.FILES)
   if form. is_valid():
      new_blog=form.save(commit=False)
      new_blog.upload_time=timezone.now()
      new_blog.save()
      return redirect ('detail',new_blog.id)
   return redirect ('main')

def question_new(request):
    form = QuestionForm()
    return render(request, 'question_new.html', {'form': form})

def question_create(request):
    form = QuestionForm(request.POST, request.FILES)
    if form.is_valid():
        new_question = form.save(commit=False)
        new_question.upload_time = timezone.now()
        new_question.save()
        return redirect('question_detail', pk=new_question.id)
    return redirect('main')


def delete(request, post_id):
  blog_delete=get_object_or_404(Post,pk=post_id)
  blog_delete.delete()               
  return redirect('main')

def update_page(request, post_id):
  blog_update=get_object_or_404(Post,pk=post_id)
  form = Postform()
  return render (request, 'update.html', {'blog_update' :blog_update})

def update (request, post_id):
  blog_update=get_object_or_404(Post,pk=post_id)
  blog_update.title=request.POST['title']
  blog_update.content=request.POST['body']
  blog_update.upload_time = timezone.now()
  blog_update.save()
  return redirect('main')

def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('main')  # 또는 'question_list'

# 수정 페이지 보여주는 함수
def question_update_page(request, question_id):
    question_update = get_object_or_404(Question, pk=question_id)
    form = QuestionForm()
    return render(request, 'question_update.html', {'question_update':question_update})

# 수정 내용 저장 처리 함수
def question_update(request, question_id):
    question_update = get_object_or_404(Question, pk=question_id)
    question_update.title = request.POST['title']
    question_update.content = request.POST['content']
    question_update.upload_time = timezone.now()  # 시간 업데이트도 같이 할 수 있어
    question_update.save()
    return redirect('question_detail', pk=question_id)


  







  


  