from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField
from django import forms
from django.contrib.auth.forms import UserCreationForm
class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}),label= '账号')
    password = forms.CharField(
        label= "密码",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

class RegisterForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}), label='账号')
    error_messages = {
        "password_mismatch": ("两个密码不能太相似"),
    }
    password1 = forms.CharField(
        label=("密码"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=('您的密码不能与其他个人信息太相似。'+'\n'+'密码必须至少包含8个字符。'+'\n'+'您的密码不能是常用密码。'+'\n'+'您的密码不能完全是数字。'),
    )
    password2 = forms.CharField(
        label=("确认密码"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=("输入与之前相同的密码进行验证。"),
    )

