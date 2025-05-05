"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from community.views import List, detail, question_detail, new, create, delete, update_page, update,question_delete,question_update_page,question_update, question_create, question_new
from community.views import *
#views.py 안의 모든 "공개된" 함수, 클래스, 변수들을 현재 파일로 가져옴
import community.views
#views.py 자체를 community.views라는 모듈로 가져옴

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List, name = "main"),
    path('<int:pk>', detail, name = "detail"),
    path('question/<int:pk>/', question_detail, name='question_detail'),
    path('new/', new,name="new"),
    path('create/', create, name="create"),
    path('delete/<int:post_id>', delete, name='delete'),
    path('update_page/<int:post_id>', update_page,name='update_page'),
    path('update/<int:post_id>', update, name='update2'),
    path('question_delete/<int:question_id>/', question_delete, name='question_delete'),
    path('question_update_page/<int:question_id>/', question_update_page, name='question_update_page'),
    path('question_update/<int:question_id>/', question_update, name='question_update'),
    path('question/new/', question_new, name='question_new'),
    path('question/create/', question_create, name='question_create'),
    path('<int:post_id>/comment',community.views.add_comment,name = 'add_comment'),
    path('<int:post_id>/like/', community.views.like_post, name='like_post'),


]
