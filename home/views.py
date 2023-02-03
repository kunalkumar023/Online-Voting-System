from django.http import HttpResponse
from .models import data,Question,choice
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from ovs import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from email import message


# Create your views here.

def home(request):
    return render(request,"index.html")

# def password(request):

#     if request.method == "POST":
#         email = request.POST['email']
#         addmission = request.POST['addmission']

#         if data.objects.filter(email=email,add=addmission):
#             return HttpResponse("you are logged in")
#             # #EMAIL 
#             # subject ="Welcome to online voting system!"
#             # message = "You are successfully registered!"
#             # from_email = settings.EMAIL_HOST_USER
#             # to_list = [email]
#             # send_mail(subject,message,from_email,to_list,fail_silently=False)

#             # #Confirmation email
#             # current_site = get_current_site(request)
#             # subject - "Confirm your email!"
#             # message2= render_to_string("email_confirmation.html",{
#             #     'name' : addmission,
#             #     'domain' : current_site.domain,
#             #     'uid' : urlsafe_base64_encode(forcebyte(myuser.pk))}
#             #     )


#     return render(request,"password.html")

def signup(request):

    if request.method == "POST":
        username=request.POST.get('username')
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if data.objects.filter(email=email,add=username):
            if User.objects.filter(username=username):
                messages.error(request,"The username is taken! try another:")
                return redirect('signup')

            myuser= User.objects.create_user(username, email, pass1)
            myuser.first_name= fname
            myuser.last_name= lname

            myuser.save()

            messages.success(request,"You are signup successfully:")
            return redirect("signin")
    return render(request,"signup.html")

def signin(request):

    if request.method =="POST":
        username= request.POST['username']
        pass1 = request.POST['pass1']

        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return HttpResponse("you are logged in")

        else:
            messages.error(request,'bad credential')
            return redirect('signin')

    return render(request,"signin.html")

def env(request):
    questions = Question.objects.all()
    return render(request,"env.html",{'questions':questions})

def vote(request,pk):
    question = Question.objects.get(id=pk)
    option = question.choices.all()
    return render(request,'vote.html',{'question':question,'option':option})
