from ast import Param
import imp
from turtle import title
from django.http import HttpResponse
from django.shortcuts import redirect, render 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout 
from home.models import Contact
from django.contrib import messages
from blog.models import post

# Create your views here.

def home(request):
    return render(request, "home/home.html")

def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']   
        print(name,email,phone,content)
        if len(name) < 4 or len(email)<3 or len(phone) < 10 or len(content)<5:
            messages.error(request , "Please fill the form Correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content = content)
            contact.save()
            messages.success(request , "Thanks Your Feedback has been submitted ")
    return render(request, "home/contact.html")

def about(request):
    return render(request, "home/about.html")

def search(request):
    query =request.GET["query"]
    if len(query) > 70:
        allPost=post.objects.none()
    else:
        allPostTitle =post.objects.filter(title__icontains=query)
        allPostContent =post.objects.filter(content__icontains=query)
        allPost =allPostTitle.union(allPostContent)



    if allPost.count() == 0:
        messages.warning(request , "Please search better Keywords")
        
    params ={"allPost": allPost , "query" : query}
    return render(request, "home/search.html" , params)

#authentiation APIs

def handelSignup(request):
    #post parameters
    if request.method =="POST":
        username = request.POST["username"] 
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]

        #checks for Error inpts
        if len(username) >10:
            messages.error(request ,"User Name must be unser 10 characters")
            return redirect("home")

        if not username.isalnum():
            messages.error(request ,"User Name must be Alphanumaric please Try again")
            return redirect("home")

        if pass1 != pass2:
            messages.error(request ,"Paasword did not match please enter correct passwords")
            return redirect("home")


        #create User 
        myuser= User.objects.create_user( username , email , pass1)
        myuser.first_name =fname 
        myuser.last_name =lname
        myuser.save()
        messages.success(request ,"Your iCoder account has been created Successully")
        return redirect("home")
    else:
        return HttpResponse("404 - Page not found")

def handelLogin(request):
    if request.method=="POST":
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user =authenticate(username= loginusername , password = loginpassword)
        if user is not None:
            login(request , user)
            messages.success(request ,"Login Successfull. ")
            return redirect("home")
        else:
            messages.error(request ,"Login failed ! Please try again ")
            return redirect("home")
    return HttpResponse("404 - Page not found")

def handelLogout(request):
    logout(request)
    messages.success(request ,"Logout Successfully. ")
    return redirect("home")
    
