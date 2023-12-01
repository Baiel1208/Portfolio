from django.shortcuts import render, redirect
from django.views.generic import DetailView
from . import models as m


# Create your views here.
def index(request):
    infouser = m.InfoUser.objects.latest("id")
    return render(request,"index.html", locals())


def about(request):
    info_me = m.About.objects.latest('id')
    skills = m.Skills.objects.all()
    experience = m.Experience.objects.all()
    education = m.Education.objects.all()

    return render(request,"about.html",locals())


def portfolio(request):
    portfolio = m.Portfolio.objects.all()
    return render(request,"portfolio.html",locals())


def contacts(request):
    infouser = m.InfoUser.objects.latest("id")
    about = m.About.objects.latest('id')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        m.Contact.objects.create(name=name, email=email, message=message)
        return redirect('index')
    return render(request,"contact.html",locals())  


def blog(request):
    blog = m.Blog.objects.all()
    return render(request,"blog.html",locals())


class BlogPostDetailView(DetailView):
    model = m.Blog
    template_name = 'blog-post.html'
    context_object_name = 'blog'
    pk_url_kwarg = 'pk'
