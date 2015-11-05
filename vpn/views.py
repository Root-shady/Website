from django.shortcuts import render
from vpn.models import User
from vpn.forms import UserForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

# The home page of the VPN  
# if the request is a POST, we process form data, if it is a GET, we show the form
def register(request):
    redirect_to = request.REQUEST.get('next', '')
    if request.method == 'POST':
        form = UserForm(request.POST)
# Have we benn provided with a valid form
        if form.is_valid():
# Svae the new User to the database 
            result = form.save(commit=True)
            user_id = result.pk   # the form.pk also works
            # call the index view
# Show the use the home page  Get the user's id (Since only the email is unique
            
            request.session['user_id'] = user_id
            request.session['username'] = request.POST['username']
# How to use if request.session.has_key('user_id') user_id = request.session.get('user_id')
            return HttpResponseRedirect(redirect_to)
        else: print(form.errors)
    else:
# If the request was not POST, display the form to enter details 
        form = UserForm()
# Bad from, no form supplied(form details)
# Render the form with error message(if any
    return render(request, 'vpn/register.html', {'form': form})

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

def logout(request):
    if request.session.has_key('user_id'):
        request.session.modified = True
        del request.session['user_id']
        del request.session['username']
       # username = None
        #redirect_url = reverse(request.META.get('HTTP_REFERER'), args=['username'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    is_active, user_id = authenticated(username, password)

    if is_active:
        request.session['username'] = username
        request.session['user_id'] =  user_id
    else:
# Print some error message 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


