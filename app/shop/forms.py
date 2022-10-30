from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)



class NewPersonalData(forms.ModelForm):
	username = forms.CharField(max_length=100,
		required=True,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш ник', 'type': 'text'}))
	email = forms.EmailField(required=True,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу почту', 'type': 'email'}))
	class Meta:
		model = User
		fields = ["username", "email",]


class DeleteUser(forms.Form):
	check = forms.BooleanField(required=False,
		widget=forms.TextInput(attrs={ 'class': 'custom-control-input', 'type': 'checkbox'}))
