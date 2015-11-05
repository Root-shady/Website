from vpn.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=50, help_text="", widget=forms.PasswordInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password', 'sex')
        # Provide an association between the ModelForm and a model
        labels = {
                    #'username': ('User'),
                }
        help_texts = {
                    'email':('例如: wnagyi163@163.com')
                }
        error_messages = {
                    'email':{
                        'invalid': ('邮件格式不对')
                        },
                }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
# Action on calling the register view again, do the data validation 
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Submit'))
        

    def clean(self):
        cleaned_data = self.cleaned_data
        if len(cleaned_data.get('password'))  < 6:
            self.add_error('password', '密码长度必须超过六位')

        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            self.add_error('confirm_password', '两次密码不一致')
            #raise forms.ValidationError(('两次密码不一致'), code="invalid")
        user = User.objects.filter(email=cleaned_data.get('email'))
        if  user:
            self.add_error('email', '邮箱已注册')





