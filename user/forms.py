from django import forms
from django.contrib.auth.models import User

class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

    def __init__(self, *args, **kwargs):
        super(UserRegister,self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {'class':'form-control','required': ''}
            self.fields[field].help_text = ''

        self.fields['password'].widget=forms.PasswordInput()
        self.fields['password'].widget.attrs = {'class':'form-control'}
        