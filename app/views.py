from django.shortcuts import render
from .models import ProfileData, About, SocialLink, Tools, Service, Project, Post, Category, Tag, PostCategorys
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
def home(request):
    # Django ORM < SQL Queries ProfileData.objects.all() 
    # profilim
    profile = ProfileData.objects.first()

    # men haqimda
    about = About.objects.first()

    # liklarim
    links = SocialLink.objects.all()

    # bilish darajalarim
    tools = Tools.objects.all()

    # klientlarim
    clients = Service.objects.all()

    projects = Project.objects.all()

    posts = Post.objects.all()

    categories = Category.objects.all()

    tags = Tag.objects.all()

    
    # ko'rsatish
    context = {'profile': profile, 'about': about, 'links': links, 'tools': tools, 'clients': clients, 'projects': projects, 'posts': posts, 'category': categories, 'tag': tags}
    return render(request, "index.html", context)


def about(request):
    tools = Tools.objects.all()
    about = About.objects.first()
    
    context = {"tools": tools, "about": about}

    return render(request, "about-us.html", context)

def blog(request):
    posts = Post.objects.all()
    links = SocialLink.objects.all()
    profile = ProfileData.objects.first()

    search = request.GET.get("search")

    if search:
        posts = posts.filter(name__icontains=search)

    paginator = Paginator(posts, 5)


    page_number = request.GET.get("page")


    page_obj = paginator.get_page(page_number)
    search = request.GET.get("search")

    # papular post list

    popular_posts = Post.objects.all()[:4]

    return render(request, "blog.html", {"posts": page_obj, 'profile': profile, 'links': links, 'popular_posts': popular_posts})



def portfolio(request):
    categories = Category.objects.all()
    portfolio = Post
    context = {'categories': categories, 'portfolio': portfolio}
    return render(request, "portfolio.html", context)


def blog_detail(request, pk):
    post = get_object_or_404(Post, id=pk)


    return render(request, "single-blog.html", {'post': post})