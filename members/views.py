from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registrations.html'
    success_url = reverse_lazy('login') 