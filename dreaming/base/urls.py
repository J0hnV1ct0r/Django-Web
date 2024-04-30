"""
Este modulo contém os paths do sistema.
"""

from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (WorkList, WorkDetail,
                    CustomLoginView, RegisterPage)
from .views import (ChallengeList, ChallengeDetail, ChallengeCreate, ChallengeUpdate,
                    ChallengeDelete)
from .views import (ReviewCreate, ReviewUpdate, ReviewDelete)
from .views import (JournalCreateView, JournalUpdate, JournalDelete)
from .views import (CommunityList, CommunityDetail, CommunityCreate,
                    CommunityUpdate, CommunityDelete)


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', ChallengeList.as_view(), name='challenges'),
    path('user/challenge/<int:pk>/', ChallengeDetail.as_view(), name='challenge'),
    path('user/challenge/create/', ChallengeCreate.as_view(), name='challenge-create'),
    path('user/challenge/update/<int:pk>/', ChallengeUpdate.as_view(), name='challenge-update'),
    path('user/challenge/delete/<int:pk>/', ChallengeDelete.as_view(), name='challenge-delete'),

    path('user/works/', WorkList.as_view(), name='works'),
    path('user/work/<int:pk>/', WorkDetail.as_view(), name='work'),

    path('user/review/create/<int:work_id>/', ReviewCreate.as_view(), name='review-create'),
    path('user/review/update/<int:pk>/', ReviewUpdate.as_view(), name='review-update'),
    path('user/review/delete/<int:pk>/', ReviewDelete.as_view(), name='review-delete'),

    path('user/journal/create/<int:challenge_id>/', JournalCreateView.as_view(), name='journal-create'),
    path('user/journal/update/<int:pk>/', JournalUpdate.as_view(), name='journal-update'),
    path('user/journal/delete/<int:pk>/', JournalDelete.as_view(), name='journal-delete'),

    path('user/communities/', CommunityList.as_view(), name='communities'),
    path('user/community/<int:pk>/', CommunityDetail.as_view(), name='community'),
    path('user/community/create/', CommunityCreate.as_view(), name='community-create'),
    path('user/community/update/<int:pk>/', CommunityUpdate.as_view(), name='community-update'),
    path('user/community/delete/<int:pk>/', CommunityDelete.as_view(), name='community-delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
