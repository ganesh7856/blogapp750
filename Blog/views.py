from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post , Comments
from .forms import PostForm,CommentsForm
from django.contrib.auth.models import User

# Create your views here.

Posts=[

    {'author':'Ganesh',
     'title':'Blog Post 1',
     'content':'First content',
     'date_posted':'7th July 2020'
     },
    {'author': 'suraj',
     'title': 'Blog Post 2',
     'content': 'Second content',
     'date_posted': '8th July 2020'
     }
]
def Home(request):
    context={'Posts': Post.objects.all() }
    return render(request,'blog/home.html',context)


def About(request):
  return render(request,'blog/about.html',{'title':'About'})



def PostFormView(request):

    if request.method == 'POST':
         form = PostForm(request.POST,request.FILES)
         if form.is_valid():
             form.save()
             return redirect('blog-name')
    else :
        form = PostForm()
    return render (request,'blog/postform.html',{'form':form})



# def Like_Post(request):
#     formdata=request.POST
#     id=int(formdata['post_id'])
#     post=Post.objects.get(id=id)
#     is_liked=False
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#         is_liked=False
#     else:
#          post.likes.add(request.user)
#          is_liked=True
#     return redirect('blog-name')

def Like_Post(request):
           post=get_object_or_404(Post,id=request.POST.get('post_id'))
           is_liked = False
           if post.likes.filter(id=request.user.id).exists():
                   post.likes.remove(request.user)
                   is_liked=False
           else:
                user=User
                post.likes.add(request.user.id)
           return redirect('blog-name')

def Post_Detail_View(request,id):
    posts=Post.objects.get(id=id)
    comments=Comments.objects.filter(post=posts,reply=None).order_by('-id')
    is_liked = False
    if posts.likes.filter(id=request.user.id).exists():
        is_liked=True
    if request.method=='POST':
        comment_form=CommentsForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            reply_id=request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs=Comments.objects.get(id=reply_id)
            comment=Comments.objects.create(post=posts,user=request.user,content=content,reply=comment_qs)
            comment.save()
            return redirect('blog-name')
    else :
        comment_form=CommentsForm()
    return render(request,'blog/postdetail.html',{'posts':posts,'is_liked':is_liked,
                                                  'total_likes':posts.total_likes,
                                                  'comments':comments,
                                                  'comment_form':comment_form})
