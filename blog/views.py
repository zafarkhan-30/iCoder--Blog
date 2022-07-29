from django.contrib import messages
from django.shortcuts import redirect, render 
from blog.models import post , BlogComment
# Create your views here.
def blogHome(request):
    allPost = post.objects.all()
    context = {"allPost":allPost}
    return render(request , "blog/blogHome.html" , context)
   

def blogPost(request, slug):
    Post = post.objects.filter(slug=slug).first()
    Post.views = Post.views + 1
    Post.save()
    context ={"Post":Post}
    return render(request , "blog/blogPost.html" , context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        Post= post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, Post=Post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")