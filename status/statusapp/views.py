from django.shortcuts import render , HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required

from statusapp.models import * 


def properties_single(request):
    return render(request,'properties-single-page.html')



def properties(reques):
    return render(reques,'properties.html') 


def contact_us(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    mobile_number = request.POST.get('mobile_number')
    message = request.POST.get('text')
    con = Contact_Us(name = name,email = email, mobile_no = mobile_number, message = message)
    con.save()
    return render(request,'contact_us.html') 

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html') 


def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')



def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')



def LogoutPage(request):
    logout(request)
    return redirect('login')