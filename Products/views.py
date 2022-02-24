from .form import *
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def about(request):
    return render(request, 'about.html' )


class ListProduct(ListView):
    model = product
    template_name = 'home.html'

class CreateProduct(CreateView):
    model = product
    form_class = adminForm
    template_name = 'modifyList.html'
    success_url = reverse_lazy('home')


class UpdateProduct(UpdateView):
    model = product
    form_class = adminForm
    template_name = 'modifyList.html'
    success_url = reverse_lazy('home')


class DeleteProduct(DeleteView):
    model = product
    form_class = adminForm
    template_name = 'VerifyDelete.html'
    success_url = reverse_lazy('home')


class buying(ListView):
    model = product
    template_name = 'buying.html'

def salir(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context )

def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, "Tu comentario ha sido enviado exitósamente. En breve recibiras respuesta de parte de nosotros.")
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'contactanos.html', {'form': form})

def sendRequest(request ):   
    user = request.user
    solicitudes = user.requests.all()
    return render(request, 'historial.html', {'user':user, 'requests':solicitudes})