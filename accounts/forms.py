from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'placeholder': 'Contanos tu manifiesto épico...'}))
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'avatar', 'bio']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
