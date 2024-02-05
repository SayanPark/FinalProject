from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    user_name = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Enter a unique username'}))
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user existed before')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('this email is existed before')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('passwords are not match')
        elif len(password1) < 8:
            raise forms.ValidationError('the password should has 8 words or more.')
        elif not any(i.isupper() for i in password1):
            raise forms.ValidationError('the password should has at least 1 capital word')
        else:
            return password1


class UserLoginFrom(forms.Form):
    user = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_user(self):
        user = self.cleaned_data['user']
        if not User.objects.filter(username=user).exists():
            raise forms.ValidationError('the username does not exist')
        return user

    def clean_password(self):
        user = self.cleaned_data.get('user')
        password = self.cleaned_data.get('password')

        if user and password:
            user_obj = User.objects.filter(username=user).first()
            if user_obj and not user_obj.check_password(password):
                raise forms.ValidationError('the password does not match with the username')

        return password


class ChangePasswordForm(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput())
    new_pass1 = forms.CharField(widget=forms.PasswordInput())
    new_pass2 = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_pass(self):
        old_pass = self.cleaned_data.get('old_pass')
        if not self.user.check_password(old_pass):
            raise forms.ValidationError("the old password is not correct")
        return old_pass

    def clean(self):
        cleaned_data = super().clean()
        new_pass1 = cleaned_data.get('new_pass1')
        new_pass2 = cleaned_data.get('new_pass2')

        if new_pass1 != new_pass2:
            raise forms.ValidationError("The new passwords do not match.")

        if len(new_pass1) < 8:
            raise forms.ValidationError("The password should have 8 characters or more.")

        if not any(i.isupper() for i in new_pass1):
            raise forms.ValidationError("The password should have at least 1 capital letter.")

        return cleaned_data
