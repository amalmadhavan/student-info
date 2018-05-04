from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


# used to create the blueprint of the form for registering users that use the site

class Userform(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField()


    class Meta:
        model = User
        fields = ['username','email',]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
       # user.accesslvl = self.cleaned_data['accesslvl']

        if commit:
            user.save()

        return user

# class LoginForm(forms.ModelForm):
