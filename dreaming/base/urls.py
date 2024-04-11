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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
