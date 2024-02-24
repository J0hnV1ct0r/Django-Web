from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Work


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('works')


class WorkList(ListView):
    model = Work
    context_object_name = 'works'


class WorkDetail(DetailView):
    model = Work
    context_object_name = 'work'
    template_name = 'base/work.html'


class WorkCreate(CreateView):
    model = Work
    fields = '__all__'
    success_url = reverse_lazy('works')


class WorkUpdate(UpdateView):
    model = Work
    fields = '__all__'
    success_url = reverse_lazy('works')


class WorkDelete(DeleteView):
    model = Work
    context_object_name = 'work'
    success_url = reverse_lazy('works')
