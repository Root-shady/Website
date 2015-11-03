from vpn.models import User
from django import forms

class UserForm(forms.ModelForm):
    confirm_passwd = forms.CharField(max_length=50, help_text="Enter the same password again")
    class Meta:
        # Provide an association between the ModelForm and a model
        fields = ('username', 'email', 'password', 'confirm_passwd', 'sex')


