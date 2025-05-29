from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from community.models import *
from community.forms import Postform, QuestionForm, Commentform

# Create your views here.

def List(request):
  posts= Post.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
  questions= Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
  return render(request, 'list.html', {'posts':posts, 'questions':questions})

def detail(request,pk):
  post_detail = get_object_or_404(Post, pk=pk)
  post_hashtag= post_detail.hashtag.all()
  like_count = post_detail.likes.count()
  return render(request, 'detail.html', {'post':post_detail,'hashtag':post_hashtag,'like_count': like_count })

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
      hashtags = request.POST['hashtags']
      hashtag = hashtags.split(', ')

      for tag in hashtag:
         new_hashtag = Hashtag()
         new_hashtag.hashtag=tag
         new_hashtag = Hashtag.objects.get_or_create(hashtag = tag)
         new_blog.hashtag.add(new_hashtag[0])
      return redirect ('detail',new_blog.id)
   return redirect ('main')

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

def add_comment(request, post_id):
   blog= get_object_or_404(Post, pk = post_id)

   if request.method =="POST":
      form = Commentform(request.POST, request.FILES)

      if form.is_valid():
         comment = form.save(commit=False)
         comment.post = blog
         comment.save()
         return redirect('detail',post_id)
   else:
      form=Commentform()
   return render(request,'add_comment.html',{'form':form})

def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    Like.objects.create(post=post)
    return redirect('detail', pk=post_id)

def question_add_comment(request, post_id):
   blog= get_object_or_404(Post, pk = post_id)

   if request.method =="POST":
      form = Commentform(request.POST)

      if form.is_valid():
         comment = form.save(commit=False)
         comment.post = blog
         comment.save()
         return redirect('detail',post_id)
   else:
      form=Commentform()
   return render(request,'add_comment.html',{'form':form})

def question_like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    Like.objects.create(post=post)
    return redirect('detail', pk=post_id)






  







  


  