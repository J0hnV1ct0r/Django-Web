from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from ..mediators.workMediator import WorkMediator
from ..models import Work


class WorkList(LoginRequiredMixin, ListView):
    """View de listagem de obras literarias."""
    model = Work
    context_object_name = 'works'
    template_name = 'base/work_front/work_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        mediator = WorkMediator(self.request)
        context['search_input'] = mediator.search_input
        context['books'] = mediator.filter_and_paginate_works(kind='Book')
        context['comics'] = mediator.filter_and_paginate_works(kind='Comic')
        context['mangas'] = mediator.filter_and_paginate_works(kind='Manga')
        return context


class WorkDetail(LoginRequiredMixin, DetailView):
    """View de detalhamento de obras e listagem de reviews."""
    model = Work
    context_object_name = 'work'
    template_name = 'base/work_front/work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        work = self.get_object()
        mediator = WorkMediator(self.request)
        context.update(mediator.get_work_reviews(work))
        return context
