from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'full_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),


        }

    def save(self, commit=True):
        user = User.objects.create_user(
            **self.cleaned_data,
        )

        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        