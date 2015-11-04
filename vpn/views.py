from django.shortcuts import render
from vpn.models import User
from vpn.forms import UserForm
# Create your views here.

# The home page of the VPN  
# if the request is a POST, we process form data, if it is a GET, we show the form
def register(request):
    context_dict = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
# Have we benn provided with a valid form
        if form.is_valid():
# Svae the new User to the database 
            form.save(commit=True)
            # call the index view
# Show the use the home page
            return index(request)
        else:
            print(form.errors)
    else:
# If the request was not POST, display the form to enter details 
        form = UserForm()
# Bad from, no form supplied(form details)
# Render the form with error message(if any
    return render(request, 'vpn/register.html', {'form': form})

def index(request):
    context_dict = {}
    return render(request, 'vpn/index.html', context_dict)


