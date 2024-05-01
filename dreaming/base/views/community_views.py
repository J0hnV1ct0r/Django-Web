from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..models import Community, CommunityReview


class CommunityList(LoginRequiredMixin, ListView):
    model = Community
    context_object_name = 'communities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['communities'] = context['communities'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context


class CommunityDetail(LoginRequiredMixin, DetailView):
    model = Community
    context_object_name = 'community'
    template_name = 'base/community.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        community = self.get_object()
        # pylint: disable=E1101
        user_reviews = CommunityReview.objects.filter(community=self.object, user=self.request.user)
        # pylint: disable=E1101
        other_reviews = CommunityReview.objects.filter(community=self.object).exclude(user=self.request.user)
        # pylint: disable=E1101
        reviews = CommunityReview.objects.filter(community=community)
        #average_score = reviews.aggregate(Avg('score'))['score__avg'] or 0
        num_reviews = reviews.count()
        context['user_reviews'] = user_reviews
        context['other_reviews'] = other_reviews
        #context['average_score'] = average_score
        context['num_reviews'] = num_reviews
        return context


class CommunityCreate(LoginRequiredMixin, CreateView):
    model = Community
    fields = ['name', 'description', 'link']
    success_url = reverse_lazy('communities')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CommunityUpdate(LoginRequiredMixin, UpdateView):
    model = Community
    fields = ['name', 'description', 'link']
    success_url = reverse_lazy('communities')
    template_name = 'base/community_update.html'


class CommunityDelete(LoginRequiredMixin, DeleteView):
    model = Community
    context_object_name = 'community'
    success_url = reverse_lazy('communities')