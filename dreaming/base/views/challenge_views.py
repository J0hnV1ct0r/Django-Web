from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..mediators.challengeMediator import ChallengeMediator
from ..models import Challenge


class ChallengeList(LoginRequiredMixin, ListView):
    """View de listagem dos desafios não completados pelo usuario."""
    model = Challenge
    context_object_name = 'challenges'
    template_name = 'base/challenge_front/challenge_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mediator = ChallengeMediator(self.request)
        context.update(mediator.get_combined_context())
        return context


class ChallengeDetail(LoginRequiredMixin, DetailView):
    """View de detalhamento de desafios de leitura."""
    model = Challenge
    context_object_name = 'challenge'
    template_name = 'base/challenge_front/challenge.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        challenge = self.get_object()
        mediator = ChallengeMediator(self.request)
        context.update(mediator.get_combined_context(challenge=challenge))
        return context


class ChallengeCreate(LoginRequiredMixin, CreateView):
    """View de criação de desafios de leitura."""
    model = Challenge
    fields = ['book', 'title', 'description']
    success_url = reverse_lazy('challenges')
    template_name = 'base/challenge_front/challenge_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChallengeUpdate(LoginRequiredMixin, UpdateView):
    """View de atualização de desafios de leitura."""
    model = Challenge
    fields = ['book', 'title', 'description', 'completed']
    success_url = reverse_lazy('challenges')
    template_name = 'base/challenge_front/challenge_update.html'


class ChallengeDelete(LoginRequiredMixin, DeleteView):
    """View de deleção de desafios de leitura do sistema."""
    model = Challenge
    context_object_name = 'challenge'
    success_url = reverse_lazy('challenges')
    template_name = 'base/challenge_front/challenge_confirm_delete.html'
