from django.core import paginator
from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog #models.py의 Blog클래스를 가져옴
from .forms import BlogForm #BlogFrom import 해주기

# Create your views here.
# all get oreder_by filter exclude .... 필요한거 찾아서 사용하기 
def home(request):
    blogs = Blog.objects.order_by('-pup_date') #최신순으로 정렬
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs = Blog.objects.filter(writer=author).order_by('-pup_date')
        #blogs = Blog.objects.exclude(writer=author) #작성자 제외하고 가져옴
        return render(request, 'home.html', {'blogs':blogs})

    paginator = Paginator(blogs, 8)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk) #객체를 갖고오던가 Not found error를 띄워줌.
    return render(request,'detail.html',{'blog':blog})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    # new_blog = Blog()#객체 생성
    # new_blog.title = request.POST['title']
    # new_blog.writer = request.POST['writer']
    # new_blog.body = request.POST['body']
    # new_blog.pup_date = timezone.now()
    # new_blog.image = request.FILES['image']
    # new_blog.save()
    #새로운 html을 만들어서 보내는게 아니기 때문에 render함수를 쓰지 않는다.
    #원래 있던 페이지로 돌아가야 하기 때문에 redirect함수를사용한다.
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)#pup_date가 빠져서 임시저장시켜줌
        new_blog.pup_date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')

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