from django.shortcuts import render, redirect
from django.forms import BaseModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Work


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('works')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('works')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('works')
        return super(RegisterPage, self).get(*args, **kwargs)


class WorkList(LoginRequiredMixin, ListView):
    model = Work
    context_object_name = 'works'


class WorkDetail(LoginRequiredMixin, DetailView):
    model = Work
    context_object_name = 'work'
    template_name = 'base/work.html'


class WorkCreate(LoginRequiredMixin, CreateView):
    model = Work
    fields = '__all__'
    success_url = reverse_lazy('works')


class WorkUpdate(LoginRequiredMixin, UpdateView):
    model = Work
    fields = '__all__'
    success_url = reverse_lazy('works')


class WorkDelete(LoginRequiredMixin, DeleteView):
    model = Work
    context_object_name = 'work'
    success_url = reverse_lazy('works')
