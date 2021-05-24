from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.accounts.models import *
from apps.cart.models import *

# Create your views here.
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from active_page import set_page_active

def signin(request):
    set_page_active("Accounts")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = authenticate(username= email, password= password)
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            # productcount = request.session.get('productcount')
            # if productcount is None:
            #     productcount = 0
            #     request.session['productcount'] = productcount

            messages.info(request,'Happy Shopping!')
            return redirect("apps.main:index")
            
        else:
            messages.warning(request,'Username and Password mismatch.')
            return redirect("apps.accounts:signin")
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
        #request.session['productcount'] = 0
        messages.info(request,'Enter Information')
        return redirect("apps.accounts:profileset")
    return render(request, "account-signup.html")

@login_required
def signout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully.')
    return redirect("apps.accounts:signin")

@login_required
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
            messages.success(request,'Information Added.')
            return redirect("apps.accounts:shippinginfo")
    else:
        messages.warning(request,'You are not signed in.')
        return redirect("apps.accounts:signin")
    return render(request, "profile-details.html", {'profile': profile, 'user': user})

@login_required
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
            messages.success(request,'Address added.')
            return redirect("apps.main:index")
    else:
        messages.warning(request,'You are not signed in.')
        return redirect("apps.accounts:signin")

    return render(request, "profile-shipping.html",{'profile': profile, 'address': address})

@login_required
def acprofile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if not request.user.is_staff:
        profile = Profile.objects.get(user=user)
        previmg=profile.image
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
            messages.info(request,'Profile Updated.')
            return redirect("apps.accounts:address")
    else:
        messages.warning(request,'You are signed in as Seller')
        return redirect("apps.accounts:signin")
    return render(request, "account-profile.html", {'profile': profile, 'user': user})

def address(request):
    profile = Profile.objects.get(id=request.user.profile.id)
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
            messages.success(request,'Address added.')
            return redirect("apps.accounts:address")
    else:
        messages.warning(request,'You are not signed in.')
        return redirect("apps.accounts:signin")

    return render(request, "account-address.html",{'profile': profile, 'address_list':address_list})


@login_required
def manageadd(request, addid):
    
        add_id = addid
        action = request.GET.get("action")
        profile = Profile.objects.get(id=request.user.profile.id)
        #address = Address.objects.filter(profile=profile).last()
        address_list= Address.objects.all()
        getaddid = request.GET.get("addid")
        address = Address.objects.filter(id=int(getaddid)).last()
        

        if request.user.is_authenticated:
            if action == "edit":
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
                    messages.success(request,'Address Edited')
                    return redirect("apps.accounts:address")

            elif action == "rem":
                address = Address.objects.filter(id=getaddid).delete()
                messages.warning(request,'Address Removed')
                return redirect("apps.accounts:address")
        else:
            messages.warning(request,'You are not log in.')
            return redirect("apps.accounts:signin")
        
        return render(request, "account-edit-address.html",{'address': address,'profile':profile})


@login_required
def orders(request):
    profile = Profile.objects.get(id=request.user.profile.id)
    orders = Order.objects.filter(cart__profile=profile).order_by("-id")
    
    return render(request, 'account-orders.html', {'orders': orders,'profile':profile})



@login_required
def orderdetail(request, orderid):
    profile= Profile.objects.get(user=request.user)
    if request.user.is_authenticated and Profile.objects.filter(user=request.user).exists():
            order_id = orderid
            order = Order.objects.get(id=order_id)
            if request.user.profile != order.cart.profile:
                return redirect("apps.accounts:orders")
    else:
        return redirect("apps.accounts:signin")
    return render(request, 'account-order-detail.html', {'order':order,'profile':profile})
