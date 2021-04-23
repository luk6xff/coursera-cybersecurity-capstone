from django import forms
from django.contrib.auth.models import User
from .models import Profile, Message


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
        widgets = {
            'date_of_birth': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image._size > 1*1024*1024:
                raise ValidationError("Image file too large ( > 1mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")


class CreateMessageForm(forms.Form):
    receiver = forms.ModelChoiceField(queryset=User.objects.all(), label='Send your message to',
                                        widget=forms.Select(attrs={'placeholder':'Choose a receiver name'}))
    message = forms.CharField(max_length=250, label='Message content',
                                widget=forms.TextInput(attrs={'placeholder': 'Write your message here...',
                                                           'size': '80'}))