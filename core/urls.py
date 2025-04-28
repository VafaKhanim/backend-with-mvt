from django.urls import path
from .views import about_page, contact_page, blog_page, furniture_page, blog_detail, subscribe, home_page
urlpatterns = [
    path('about/', about_page, name = 'about_page'),
    path('contact/', contact_page, name = 'contact_page'),
    path('blog/', blog_page, name = 'blog_page'),
    path('furniture/', furniture_page, name = 'furniture_page'),
    path('post/<int:post_id>/', blog_detail, name='blog_detail'),
    path('subscribe/', subscribe, name='subscribe'),
    path('', home_page, name = 'home_page')

    ]