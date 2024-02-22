from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Work


# Create your views here.
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
