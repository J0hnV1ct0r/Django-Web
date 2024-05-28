from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from ..models import Work, Review


class WorkList(LoginRequiredMixin, ListView):
    """View de listagem de obras literarias."""
    model = Work
    context_object_name = 'works'
    template_name = 'base/work_front/work_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['works'] = context['works'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context


class WorkDetail(LoginRequiredMixin, DetailView):
    """View de detalhamento de obras e listagem de reviews."""
    model = Work
    context_object_name = 'work'
    template_name = 'base/work_front/work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        work = self.get_object()
        # pylint: disable=E1101
        user_reviews = Review.objects.filter(work=self.object, user=self.request.user)
        # pylint: disable=E1101
        other_reviews = Review.objects.filter(work=self.object).exclude(user=self.request.user)
        paginator = Paginator(other_reviews, 10)
        num_pages = self.request.GET.get('page')
        try:
            pages = paginator.page(num_pages)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        # pylint: disable=E1101
        reviews = Review.objects.filter(work=work)
        average_score = reviews.aggregate(Avg('score'))['score__avg'] or 0

        num_reviews = reviews.count()

        context['user_reviews'] = user_reviews
        context['other_reviews'] = other_reviews
        context['average_score'] = average_score
        context['pages'] = pages
        context['num_reviews'] = num_pages
        return context
