from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..models import Challenge, Journal


class ChallengeList(LoginRequiredMixin, ListView):
    """View de listagem dos desafios não completados pelo usuario."""
    model = Challenge
    context_object_name = 'challenges'
    template_name = 'base/challenge_front/challenge_list.html'

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
    """View de detalhamento de desafios de leitura."""
    model = Challenge
    context_object_name = 'challenge'
    template_name = 'base/challenge_front/challenge.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        challenge = self.get_object()
        # pylint: disable=E1101
        journal_entries = Journal.objects.filter(challenge=challenge).order_by('created')
        paginator = Paginator(journal_entries, 1)
        num_pages = self.request.GET.get('page')
        try:
            pages = paginator.page(num_pages)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        context['pages'] = pages
        context['num_reviews'] = num_pages
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
    template_name = 'base/challenge_front/challenge_form.html'


class ChallengeDelete(LoginRequiredMixin, DeleteView):
    """View de deleção de desafios de leitura do sistema."""
    model = Challenge
    context_object_name = 'challenge'
    success_url = reverse_lazy('challenges')
    template_name = 'base/challenge_front/challenge_confirm_delete.html'
