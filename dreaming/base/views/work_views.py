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

        books = context['works'].filter(kind='Book')
        comics = context['works'].filter(kind='Comic')
        mangas = context['works'].filter(kind='Manga')

        books_paginator = Paginator(books, 3)
        books_num_pages = self.request.GET.get('page')
        try:
            books_pages = books_paginator.page(books_num_pages)
        except PageNotAnInteger:
            books_pages = books_paginator.page(1)
        except EmptyPage:
            books_pages = books_paginator.page(books_paginator.num_pages)

        comics_paginator = Paginator(comics, 3)
        comics_num_pages = self.request.GET.get('page')
        try:
            comics_pages = comics_paginator.page(comics_num_pages)
        except PageNotAnInteger:
            comics_pages = comics_paginator.page(1)
        except EmptyPage:
            comics_pages = comics_paginator.page(comics_paginator.num_pages)

        mangas_paginator = Paginator(mangas, 3)
        mangas_num_pages = self.request.GET.get('page')
        try:
            mangas_pages = mangas_paginator.page(mangas_num_pages)
        except PageNotAnInteger:
            mangas_pages = mangas_paginator.page(1)
        except EmptyPage:
            mangas_pages = mangas_paginator.page(comics_paginator.num_pages)

        context['search_input'] = search_input
        context['books'] = books_pages
        context['comics'] = comics_pages
        context['mangas'] = mangas_pages
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
