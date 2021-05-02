from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from apps.accounts.models import *
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

        user = User.objects.create_user(
            first_name=firstname, last_name=lastname, username=username, email=email, password=password)
        Profile.objects.create(user=user)
        user.save()
        login(request, user)
        return redirect("apps.accounts:profileset")
    return render(request, "account-signup.html")


def signout(request):
    logout(request)
    return redirect("apps.main:index")


def profileset(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)
    previmg=profile.image
    if request.user.is_authenticated:
        if request.method == 'POST':

            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
            user.email = request.POST.get('emailadd')
            user.save(update_fields=['first_name', 'last_name', 'email'])

            profile.mob_no = request.POST.get('phoneno')
            profile.gender = request.POST.get('gender')
            profile.image = request.FILES.get('img')
            
            newimg=profile.image
            
            if str(newimg) == '':
               profile.image = previmg               

            profile.save(update_fields=['mob_no', 'gender', 'image'])
            return redirect("apps.accounts:shippinginfo")
    else:
        return redirect("apps.accounts:signin")
    return render(request, "profile-details.html", {'profile': profile, 'user': user})


def shippingset(request):
    profile = Profile.objects.get(id=request.user.profile.id)
    address= Address.objects.filter(profile=profile).last()
    if request.user.is_authenticated:
        if request.method == 'POST':
            addline = request.POST.get('addline')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('zipcode')
            
            address, created = Address.objects.update_or_create(
                profile_id=profile.id,addline=addline, city=city, state=state, pincode=pincode,
                defaults={'addline':addline, 'city':city, 'state':state, 'pincode':pincode, 'isprimary':True},
            )
            return redirect("apps.main:index")
    else:
        return redirect("apps.accounts:signin")

    return render(request, "profile-shipping.html",{'profile': profile, 'address': address})


def acprofile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)
    previmg=profile.image
    if request.user.is_authenticated:
        if request.method == 'POST':
            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
            user.email = request.POST.get('emailadd')
            user.save(update_fields=['first_name', 'last_name', 'email'])
            profile.mob_no = request.POST.get('phoneno')
            profile.gender = request.POST.get('gender')
            profile.image = request.FILES.get('img')
            
            
            newimg=profile.image
            
            if str(newimg) == '':
                profile.image = previmg               
            profile.save(update_fields=['mob_no', 'gender', 'image'])
            return redirect("apps.accounts:address")
    else:
        return redirect("apps.accounts:signin")
    return render(request, "account-profile.html", {'profile': profile, 'user': user})

def address(request):
    profile = Profile.objects.get(id=request.user.profile.id)
    address= Address.objects.filter(profile=profile).last()
    address_list= Address.objects.all().order_by('-id')
    if request.user.is_authenticated:
        if request.method == 'POST':
            addline = request.POST.get('addline')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('zipcode')
            isprimary = request.POST.get('primary')
            if isprimary == 'on':
                isprimary=True
                addlist=Address.objects.filter(profile=profile)
                addlist.update(isprimary=False)
            else:
                isprimary=False
            address, created = Address.objects.update_or_create(
                addline=addline, city=city, state=state, pincode=pincode,isprimary=isprimary, profile_id=profile.id,
                defaults={'addline':addline, 'city':city, 'state':state, 'pincode':pincode,'isprimary':isprimary, 'profile_id':profile.id},
            )
            #address = Address.objects.create(addline=addline, city=city, state=state, pincode=pincode,isprimary=isprimary, profile_id=profile.id)
            
            return redirect("apps.accounts:address")
    else:
        return redirect("apps.accounts:signin")

    return render(request, "account-address.html",{'profile': profile, 'address': address, 'address_list':address_list})



def manageadd(request, addid):
    
        add_id = addid
        action = request.GET.get("action")
        profile = Profile.objects.get(id=request.user.profile.id)
        #address = Address.objects.filter(profile=profile).last()
        address_list= Address.objects.all()
        getaddid = request.GET.get("addid")
        address = Address.objects.filter(id=int(getaddid)).last()
        

        if action == "edit":
            if request.user.is_authenticated:
                print('edited')
                if request.method == 'POST':
                    addline = request.POST.get('addline')
                    city = request.POST.get('city')
                    state = request.POST.get('state')
                    pincode = request.POST.get('zipcode')
                    isprimary = request.POST.get('primary')
                    if isprimary == 'on':
                        isprimary=True
                        addlist=Address.objects.filter(profile=profile)
                        addlist.update(isprimary=False)
                    else:
                        isprimary=False
                    address, created = Address.objects.update_or_create(
                        id=add_id,
                        defaults={'addline':addline, 'city':city, 'state':state, 'pincode':pincode,'isprimary':isprimary, 'profile_id':profile.id},
                    )
                    #address = Address.objects.create(addline=addline, city=city, state=state, pincode=pincode,isprimary=isprimary, profile_id=profile.id)
                    
                    return redirect("apps.accounts:address")

        elif action == "rem":
            address = Address.objects.filter(id=getaddid).delete()
            return redirect("apps.accounts:address")

        else:
            pass
        return render(request, "account-edit-address.html",{'address': address})