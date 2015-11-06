from django.shortcuts import render
from vpn.models import User
from vpn.forms import UserForm, UserProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# The home page of the VPN  
# if the request is a POST, we process form data, if it is a GET, we show the form
def register(request):
    redirect_to = request.REQUEST.get('next', '')
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

# Have we benn provided with a valid form??
        if user_form.is_valid() and profile_form.is_valid():
# Save the new User to the database 
            user = user_form.save(commit=True)
            user_id = user.pk   # the form.pk also works
# encry the password
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
# Adding the OneToOne relationship between user and userprofile
            profile.user = user
            profile.save()
# Once successfully registered
#request.session['user_id'] = user_id
#request.session['username'] = request.POST['username']
# How to use if request.session.has_key('user_id') user_id = request.session.get('user_id')
            #messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            #user = authenticate(username=user.username, password=user.password)
            if new_user:
                if new_user.is_active:
                    login(request, new_user)
                    #login(request, user)
                    print("You got here")
                    #messages.success(request, 'Profile details updated.')
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponse("Your Rango account is disabled.")
            else:
                return HttpResponse("Something wrong with the register process")
        else: print(user_form.errors, profile_form.errors)
    else:
# If the request was not POST, display the form to enter details 
        user_form = UserForm()
        profile_form = UserProfileForm()
# Bad from, no form supplied(form details)
# Render the form with error message(if any
    return render(request, 'vpn/register.html', {'user_form': user_form, 'profile_form':profile_form})

def index(request):
    username = None
    user_id = None
    if request.session.has_key('user_id'):
        user_id = request.session.get('user_id')
        username = request.session.get('username')
    
    context_dict = {
                'username': username, 
                'user_id': user_id,
            }
    return render(request, 'vpn/index.html', context_dict)

def user_logout(request):
   # if request.session.has_key('user_id'):
   #     request.session.modified = True
   #     del request.session['user_id']
   #     del request.session['username']
       # username = None
        #redirect_url = reverse(request.META.get('HTTP_REFERER'), args=['username'])
    logout(request)
# Return to the original page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
# if we have a User object, the detail are correct, if None, no user with matching credentials was found
        if user:
           if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            #print("Invalid login details:{0}, {1}".format(username, password))
            messages.error(request, "用户名、密码组合错误， 请重新尝试登录")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            #return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'vpn/index')

