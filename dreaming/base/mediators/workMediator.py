from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Avg
from ..models import Work, Review

class WorkMediator:
    def __init__(self, request):
        self.request = request
        self.search_input = request.GET.get('search-area') or ''

    def filter_and_paginate_works(self, kind=None):
        """Filtra e pagina as obras literárias."""
        works = Work.objects.all()

        if self.search_input:
            works = works.filter(title__startswith=self.search_input)

        if kind:
            works = works.filter(kind=kind)

        paginator = Paginator(works, 3)
        page_number = self.request.GET.get('page')

        try:
            pages = paginator.page(page_number)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        return pages

    def get_work_reviews(self, work):
        """Obtém as revisões de uma obra e calcula a média e número de reviews."""
        user_reviews = Review.objects.filter(work=work, user=self.request.user)
        other_reviews = Review.objects.filter(work=work).exclude(user=self.request.user)
        paginator = Paginator(other_reviews, 10)
        page_number = self.request.GET.get('page')

        try:
            pages = paginator.page(page_number)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        average_score = Review.objects.filter(work=work).aggregate(Avg('score'))['score__avg'] or 0
        num_reviews = Review.objects.filter(work=work).count()

        return {
            'user_reviews': user_reviews,
            'other_reviews': other_reviews,
            'pages': pages,
            'average_score': average_score,
            'num_reviews': num_reviews
        }