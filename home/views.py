from django.http import HttpResponse
from .models import data, Question, choice, Voter
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from ovs import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from email import message


# Create your views here.

def home(request):
    return render(request, "index.html")

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
        username = request.POST.get('username')
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if data.objects.filter(email=email, add=username):
            if data.objects.filter(username=username):
                messages.error(request, "The username is taken! try another:")
                # return redirect('signup')
                return HttpResponse("Username is already taken!")

            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()

            messages.success(request, "You are signup successfully:")
            return redirect("signin")

        else:
            messages.error(
                request, "Enter email or addmission number is wrong")

    return render(request, "signup.html")


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect("env")

        else:
            messages.error(request, 'bad credential')
            return redirect('signin')

    return render(request, "signin.html")


def env(request):
    questions = Question.objects.all()
    return render(request, "env.html", {'questions': questions})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def vote(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    # current_user = request.user
    # userid = current_user.username
    # if request.method == 'POST':
    #     if Voter.objects.filter(voter=userid, question=question):
    #         # messages.error("You are already voted:")
    #         return HttpResponse("voted")

    #     else:
    #         newvoter = Voter(voter=userid, question=question)
    #         newvoter.save()
    #         input = request.POST["choice"]
    #         selection_option = options.get(id=input)
    #         selection_option.vote += 1
    #         selection_option.save()

    return render(request, 'vote.html', {'question': question, 'options': options})

@login_required(login_url='/')
def result(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    current_user = request.user
    userid = current_user.username
    if request.method == 'POST':
        if Voter.objects.filter(voter=userid, question=question):
            messages.error(request,"You can't vote,You have already voted:")
            return redirect("env")

        else:
            newvoter = Voter(voter=userid, question=question)
            newvoter.save()
            input = request.POST["choice"]
            selection_option = options.get(id=input)
            selection_option.vote += 1
            selection_option.save()

    return render(request,"result.html",{'question':question,'options':options})