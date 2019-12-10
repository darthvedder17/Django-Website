from django.shortcuts import render

posts = [
    {'author' : 'CoreyMS' ,
     'title' : 'Blog Post 1' ,
     'content' : 'First post Content',
     'date_posted' : 'August 27, 2018'

    },
    {'author': 'Janet Brown',
     'title': 'Blog Post 2',
     'content': 'Second post Content',
     'date_posted': 'August 28, 2018'
     },
]





def home(request):
    context = {
     'posts' : posts
        }
    return render(request , 'blog/home.html',context)

def about(request):
    return render(request , 'blog/about.html' , {'title' : 'About'})