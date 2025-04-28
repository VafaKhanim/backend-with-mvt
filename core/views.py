from django.shortcuts import render, redirect
from .forms import ContactForm, SubscribeForm
from .models import Contact, Blog, Furnitures, Subscribe
# Create your views here.

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')

            Contact.objects.create(
                name = name,
                email = email,
                phone = phone,
                message = message
            )


    return render(request, 'contact.html')


def blog_page(request):
    posts = Blog.objects.all()
    return render(request, 'blog.html', {'posts':posts})

def furniture_page(request):
    furnitures = Furnitures.objects.all()
    return render(request, 'furnitures.html', {'furnitures': furnitures})


def blog_detail(request, post_id):
    try:
        post = Blog.objects.get(pk=post_id)
    except Blog.DoesNotExist:
        raise Http404("Post not found")
    return render(request, 'blog_detail.html', {'post': post})




def subscribe(request):

    if request.method == 'POST':
        form = SubscribeForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')

            Subscribe.objects.create(
                email = email,
            )

    return redirect(request.META.get("HTTP_REFERER", '/'))


def home_page(request):
        latest_furniture = Furnitures.objects.order_by('-id')[:3]
        latest_blogs = Blog.objects.order_by('-id')[:3]
        return render(request, 'index.html', {'latest_furniture': latest_furniture, 'latest_blogs': latest_blogs})