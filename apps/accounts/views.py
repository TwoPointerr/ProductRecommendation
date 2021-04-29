from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# Create your views here.

def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = authenticate(username= email, password= password)
        user = auth.authenticate(username = username, password = password)
        print(user)
        if user is not None:

            login(request, user)
            print("logged in")
            return redirect("apps.main:index")
            
        else:
            print("not logged in")
            
        
    return render(request, "account-signin.html") 

def signup(request):

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = password)
        user.save()
    return render(request, "account-signup.html") 

def signout(request):                                                   

    logout(request)
    return redirect("apps.main:index")


