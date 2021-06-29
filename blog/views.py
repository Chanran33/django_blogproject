from django.shortcuts import render,redirect, get_object_or_404
from .models import Blog #models.py의 Blog클래스를 가져옴
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects.all() #블로그 class에 있는 객체들을 싹다 갖고와라
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) #객체를 갖고오던가 Not found error를 띄워줌.
    return render(request,'detail.html',{'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()#객체 생성
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pup_date = timezone.now()
    new_blog.save()
    #새로운 html을 만들어서 보내는게 아니기 때문에 render함수를 쓰지 않는다.
    #원래 있던 페이지로 돌아가야 하기 때문에 redirect함수를사용한다.
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id=id) #받아온 id값과 같은 객체를 가져옴
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pup_date = timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')