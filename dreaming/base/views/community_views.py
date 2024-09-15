from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..mediators.communityMediator import CommunityMediator
from ..models import Community


class CommunityList(LoginRequiredMixin, ListView):
    model = Community
    context_object_name = 'communities'
    template_name = 'base/community_front/community_list.html'

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
    template_name = 'base/community_front/community.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mediator = CommunityMediator(self.object)
        context['user_reviews'] = mediator.get_user_reviews(self.request.user)
        context['other_reviews'] = mediator.get_other_reviews(self.request.user)
        context['likes'] = mediator.get_likes_count()
        context['deslikes'] = mediator.get_dislikes_count()

        return context


class CommunityCreate(LoginRequiredMixin, CreateView):
    model = Community
    fields = ['name', 'description', 'link']
    success_url = reverse_lazy('communities')
    template_name = 'base/community_front/community_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CommunityUpdate(LoginRequiredMixin, UpdateView):
    model = Community
    fields = ['name', 'description', 'link']
    success_url = reverse_lazy('communities')
    template_name = 'base/community_front/community_update.html'


class CommunityDelete(LoginRequiredMixin, DeleteView):
    model = Community
    context_object_name = 'community'
    success_url = reverse_lazy('communities')
    template_name = 'base/community_front/community_confirm_delete.html'
