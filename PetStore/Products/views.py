from re import template
from .form import adminForm
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import products
from django.urls import reverse_lazy

# Create your views here.
def about(request):
    return render(request, 'about.html' )

class ListProduct(ListView):
    model = products
    template_name = 'home.html'

class CreateProduct(CreateView):
    model = products
    form_class = adminForm
    template_name = 'modifyList.html'
    success_url = reverse_lazy('home')

class UpdateProduct(UpdateView):
    model = products
    form_class = adminForm
    template_name = 'modifyList.html'
    success_url = reverse_lazy('home')

class DeleteProduct(DeleteView):
    model = products
    form_class = adminForm
    template_name = 'VerifyDelete.html'
    success_url = reverse_lazy('home')

class buying(ListView):
    model = products
    template_name = 'buying.html'