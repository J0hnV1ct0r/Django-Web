from ..models import CommunityReview

class CommunityMediator:
    def __init__(self, community):
        self.community = community

    def get_user_reviews(self, user):
        # Lógica para obter as revisões do usuário para a comunidade
        return CommunityReview.objects.filter(community=self.community, user=user)

    def get_other_reviews(self, user):
        # Lógica para obter as revisões de outros usuários
        return CommunityReview.objects.filter(community=self.community).exclude(user=user)

    def get_likes_count(self):
        # Lógica para contar os "likes" da comunidade
        return CommunityReview.objects.filter(community=self.community, like=True).count()

    def get_dislikes_count(self):
        # Lógica para contar os "deslikes" da comunidade
        return CommunityReview.objects.filter(community=self.community, like=False).count()