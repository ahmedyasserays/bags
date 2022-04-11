from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


from .models import page_acces


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')


    def clean_email(self):
        email = self.cleaned_data['email']
        user_exists = User.objects.filter(email=email).exists()
        if user_exists:
            raise ValidationError('User with this email already exists')
        return email
    
    def clean_password(self):
        validate_password(self.cleaned_data['password'])
        return self.cleaned_data['password']
    
    def save(self, commit=True):
        instance = super().save(commit)
        instance.set_password(self.cleaned_data['password'])
        if commit:
            instance.save()
        return instance


class PagesAccessForm(forms.ModelForm):
    class Meta:
        model = page_acces
        exclude = ('user', 'admin')
