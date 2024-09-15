from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from ..models import Challenge, Journal

class ChallengeMediator:
    def __init__(self, request):
        self.request = request
        self.search_input = request.GET.get('search-area') or ''

    def get_context_for_challenge_list(self):
        """Obtém o contexto para a view de listagem de desafios."""
        challenges = Challenge.objects.filter(user=self.request.user)
        count = challenges.filter(completed=False).count()

        if self.search_input:
            challenges = challenges.filter(title__startswith=self.search_input)

        return {
            'challenges': challenges,
            'count': count,
            'search_input': self.search_input
        }

    def get_context_for_challenge_detail(self, challenge):
        """Obtém o contexto para a view de detalhamento de desafios."""
        journal_entries = Journal.objects.filter(challenge=challenge).order_by('created')
        paginator = Paginator(journal_entries, 1)
        page_number = self.request.GET.get('page')

        try:
            pages = paginator.page(page_number)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        return {
            'pages': pages,
            'num_reviews': page_number
        }

    def get_combined_context(self, challenge=None):
        """Combina o contexto para as views de listagem e detalhe de desafios."""
        if challenge:
            return self.get_context_for_challenge_detail(challenge)
        else:
            return self.get_context_for_challenge_list()