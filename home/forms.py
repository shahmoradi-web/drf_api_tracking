from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label=' Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise ValidationError('پسورد ها مطابقت ندارد')
        return cd['password2']

    def clean_email(self):
        email= self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email already exists')
        return email
