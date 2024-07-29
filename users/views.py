from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterUserForm


class UserCreate(LoginRequiredMixin, CreateView):
    template_name = 'users/create_user.html'
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

    @login_required()
    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = user.first_name.title()
            user.last_name = user.last_name.title()
            user.save()

            return redirect('login')