from vpn.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=50, help_text="不少于六位密码", widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=50, help_text="重复上面的密码", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        # Provide an association between the ModelForm and a model
        labels = {
                    #'username': ('User'),
                }
        help_texts = {
                    'email':('例如: wnagyi163@163.com'),
                    'username':('少于30个字符,只使用数字,字母 @/.+/-/_'),
                }
        error_messages = {
                    'username':{
                        'required':('用户名必须填写'),  
                        'invalid':('用户名已经存在')
                        },
                    'email':{
                        'invalid': ('邮件格式不对'),
                        'required':('邮件必须填写'),
                        },
                    'password':{
                        'required':('密码必须填写')
                        },
                    'confirm_password':{
                        'required':('必须填写')
                        },
                }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_method = 'post'
# Action on calling the register view again, do the data validation 
        #self.helper.form_action = ''
        self.helper.form_tag = False
        

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        if password and len(password) < 6:
            self.add_error('password', '密码长度必须超过六位')

        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            self.add_error('confirm_password', '两次密码不一致')
            #raise forms.ValidationError(('两次密码不一致'), code="invalid")
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('sex',)
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_tag = False

#class LoginForm(forms.ModelForm):
   # username = models.CharField(max_length=30, required=True)
   # password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
   # class = Meta:
   #     field = ('username', 'password',)
    #def __init__(self, *args, **kwargs):
    #    super(LoginForm, self).__init__(*args, **kwargs)
    #    self.helper = FormHelper()
    #    self.helper.method = 'post'
    #    self.helper.action = ''
