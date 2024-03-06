from django.shortcuts import render, redirect
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django.forms import BaseModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils.decorators import method_decorator

from .models import Work, Challenge, Review


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('challenges')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('challenges')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('challenges')
        return super(RegisterPage, self).get(*args, **kwargs)


class ChallengeList(LoginRequiredMixin, ListView):
    model = Challenge
    context_object_name = 'challenges'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['challenges'] = context['challenges'].filter(user=self.request.user)
        context['count'] = context['challenges'].filter(completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['challenges'] = context['challenges'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context


class ChallengeDetail(LoginRequiredMixin, DetailView):
    model = Challenge
    context_object_name = 'challenge'
    template_name = 'base/challenge.html'


class ChallengeCreate(LoginRequiredMixin, CreateView):
    model = Challenge
    fields = ['book', 'title', 'description', 'page_per_day', 'completed']
    success_url = reverse_lazy('challenges')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ChallengeCreate, self).form_valid(form)


class ChallengeUpdate(LoginRequiredMixin, UpdateView):
    model = Challenge
    fields = ['book', 'title', 'description', 'page_per_day', 'completed']
    success_url = reverse_lazy('challenges')


class ChallengeDelete(LoginRequiredMixin, DeleteView):
    model = Challenge
    context_object_name = 'challenge'
    success_url = reverse_lazy('challenges')


class WorkList(LoginRequiredMixin, ListView):
    model = Work
    context_object_name = 'works'
    success_url = reverse_lazy('works')


class WorkDetail(LoginRequiredMixin, DetailView):
    model = Work
    context_object_name = 'work'
    template_name = 'base/work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        work = self.get_object()
        user_reviews = Review.objects.filter(work=self.object, user=self.request.user)
        other_reviews = Review.objects.filter(work=self.object).exclude(user=self.request.user)
        reviews = Review.objects.filter(work=work)
        average_score = reviews.aggregate(Avg('score'))['score__avg'] or 0
        num_reviews = reviews.count()
        context['user_reviews'] = user_reviews
        context['other_reviews'] = other_reviews
        context['average_score'] = average_score
        context['num_reviews'] = num_reviews
        return context


class WorkCreate(LoginRequiredMixin, CreateView):
    model = Work
    fields = '__all__'
    template_name = 'base/review_form.html'
    success_url = reverse_lazy('works')


class WorkUpdate(LoginRequiredMixin, UpdateView):
    model = Work
    fields = '__all__'
    success_url = reverse_lazy('works')


class WorkDelete(LoginRequiredMixin, DeleteView):
    model = Work
    context_object_name = 'work'
    success_url = reverse_lazy('works')


class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'review', 'score']
    success_url = reverse_lazy('works')

    def form_valid(self, form):
        work = get_object_or_404(Work, pk=self.kwargs['work_id'])
        form.instance.work = work
        form.instance.user = self.request.user
        return super(ReviewCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('work', kwargs={'pk': self.object.work.pk})


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['title', 'review', 'score']
    context_object_name = 'review'

    def get_success_url(self):
        return reverse_lazy('work', kwargs={'pk': self.object.work.pk})


class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    context_object_name = 'review'

    def get_success_url(self):
        return reverse_lazy('work', kwargs={'pk': self.object.work.pk})
