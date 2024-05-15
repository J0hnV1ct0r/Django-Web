from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Community, CommunityReview


class CommunityReviewCreate(LoginRequiredMixin, CreateView):
    """View de criação de review de comunidade."""
    model = CommunityReview
    fields = ['title', 'review', 'like']
    template_name = 'base/community_review_delete/community_review_form.html'

    def form_valid(self, form):
        community = get_object_or_404(Community, pk=self.kwargs['community_id'])
        form.instance.community = community
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('community', kwargs={'pk': self.object.community.pk})


class CommunityReviewUpdate(LoginRequiredMixin, UpdateView):
    """View de atualização de review da comunidade."""
    model = CommunityReview
    fields = ['title', 'review', 'like']
    context_object_name = 'review'
    template_name = 'base/community_review_delete/community_review_update.html'

    def get_success_url(self):
        return reverse_lazy('community', kwargs={'pk': self.object.community.pk})


class CommunityReviewDelete(LoginRequiredMixin, DeleteView):
    """View de deleção de review da comunidade."""
    model = CommunityReview
    context_object_name = 'review'
    template_name = 'base/community_review_delete/community_review_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('community', kwargs={'pk': self.object.community.pk})
