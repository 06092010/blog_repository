from django.urls import path
from .views import home, about, blog, portfolio, blog_detail

urlpatterns = [
    path('', home),
    path('about/', about),
    path('blog/', blog, name="blog"),
    path('portfolio/', portfolio),
    path('blog/<int:pk>/', blog_detail, name="blog_detail")
]