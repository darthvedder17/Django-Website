from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    #Used to specify the home page
    path('' , views.home , name = 'blog-home' ),
    path('about/', views.about , name = 'blog-about')

]