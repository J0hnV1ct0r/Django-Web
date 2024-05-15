
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..models import Challenge, Journal


class JournalCreateView(LoginRequiredMixin, CreateView):
    """View de criação de journal."""
    model = Journal
    fields = ['entry_name', 'entry']
    template_name = 'base/journal_front/journal_form.html'

    def form_valid(self, form):
        challenge = get_object_or_404(Challenge, pk=self.kwargs['challenge_id'])
        form.instance.challenge = challenge
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('challenge', kwargs={'pk': self.object.challenge.pk})


class JournalUpdate(LoginRequiredMixin, UpdateView):
    """View de atualização de journal."""
    model = Journal
    fields = ['entry_name', 'entry']
    context_object_name = 'journal'
    template_name = 'base/journal_front/journal_update.html'

    def get_success_url(self):
        return reverse_lazy('challenge', kwargs={'pk': self.object.challenge.pk})


class JournalDelete(LoginRequiredMixin, DeleteView):
    """View de deleção de journal do sistema."""
    model = Journal
    context_object_name = 'journal'
    template_name = 'base/journal_front/journal_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('challenge', kwargs={'pk': self.object.challenge.pk})
