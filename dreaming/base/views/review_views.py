
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Work, Review


class ReviewCreate(LoginRequiredMixin, CreateView):
    """View de criação de review."""
    model = Review
    fields = ['title', 'review', 'score']
    success_url = reverse_lazy('works')

    def form_valid(self, form):
        work = get_object_or_404(Work, pk=self.kwargs['work_id'])
        form.instance.work = work
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('work', kwargs={'pk': self.object.work.pk})


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    """View de atualização de review."""
    model = Review
    fields = ['title', 'review', 'score']
    context_object_name = 'review'

    def get_success_url(self):
        return reverse_lazy('work', kwargs={'pk': self.object.work.pk})


class ReviewDelete(LoginRequiredMixin, DeleteView):
    """View de deleção de review do sistema."""
    model = Review
    context_object_name = 'review'

    def get_success_url(self):
        return reverse_lazy('work', kwargs={'pk': self.object.work.pk})
