from django import forms
from django.contrib.auth.models import User


from .models import Profile


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Введите логин', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Введите пароль', required=True,
                                help_text='Пароль не должен быть простым',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Введите логин', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):

    img = forms.ImageField(label='Загрузить фото', required=False,
                           widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['img']
