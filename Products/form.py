from .models import Post, product
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class adminForm(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label= 'Correo Electrónico'),
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput),
    password2= forms.CharField(label = 'Confirmar Contraseña', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:" " for k in fields}

class PostForm(forms.ModelForm):
    content = forms.CharField(label = '', widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Que estas pensando?\n\tDeja tus sugerencias...'}), required=True)

    class Meta:
        model = Post
        fields = ['content']