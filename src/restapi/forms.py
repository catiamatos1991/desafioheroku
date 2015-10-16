__author__ = 'P057668'

from django import forms

from restapi.models import  SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
            model = SignUp
            fields=['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')

        if not extension == "com":
            raise forms.ValidationError("Please use a valid .com email address")
        return email

    def clean_fullname(self):
        full_name = self.claned_data.get('fullname')
        return full_name

