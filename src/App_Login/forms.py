from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget= forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    uva_id = forms.CharField(required=True, label="", widget= forms.TextInput(attrs={'placeholder':'UVA Id'}))
    codeforces_username = forms.CharField(required=True, label="", widget= forms.TextInput(attrs={'placeholder':'Codeforces Username'}))

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2','uva_id','codeforces_username')

class EditProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(label="Set a Profile Picture", required=False) 
    class Meta:
        model = UserProfile
        exclude = ('user',)  