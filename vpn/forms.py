from vpn.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserForm(forms.ModelForm):
    confirm_passwd = forms.CharField(max_length=50, help_text="", widget=forms.PasswordInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    class Meta:
        model = User
        # Provide an association between the ModelForm and a model
        fields = ('username', 'email', 'password', 'confirm_passwd', 'sex')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
# Action on calling the register view again, do the data validation 
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Submit'))



