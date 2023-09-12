from django import forms
from .models import Users
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class SignInForms(AuthenticationForm):
    class Meta:
        model = Users
        fields = ["username", "password"]
    
class SignUpForms(UserCreationForm):
    gender_cho = [("MAN","MAN"),("WOMAN","WOMAN")]
    gender = forms.ChoiceField(choices=gender_cho)
    class Meta:
        model = Users
        fields = ["username", "email", "password1", "password2", "gender"]
