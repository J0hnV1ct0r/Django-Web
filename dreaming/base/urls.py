from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (WorkList, WorkDetail, WorkCreate, WorkUpdate, DeleteView, CustomLoginView, RegisterPage,
                    ChallengeList,
                    ChallengeDetail, ChallengeCreate, ChallengeUpdate, ChallengeDelete, ReviewCreate, ReviewUpdate, ReviewDelete)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', ChallengeList.as_view(), name='challenges'),
    path('challenge/<int:pk>/', ChallengeDetail.as_view(), name='challenge'),
    path('challenge-create/', ChallengeCreate.as_view(), name='challenge-create'),
    path('challenge-update/<int:pk>/', ChallengeUpdate.as_view(), name='challenge-update'),
    path('challenge-delete/<int:pk>/', ChallengeDelete.as_view(), name='challenge-delete'),

    path('works/', WorkList.as_view(), name='works'),
    path('work/<int:pk>/', WorkDetail.as_view(), name='work'),
    path('work-create/', WorkCreate.as_view(), name='work-create'),
    path('work-update/<int:pk>/', WorkUpdate.as_view(), name='work-update'),
    path('work-delete/<int:pk>/', DeleteView.as_view(), name='work-delete'),

    path('review-create/<int:work_id>/', ReviewCreate.as_view(), name='review-create'),
    path('review-update/<int:pk>/', ReviewUpdate.as_view(), name='review-update'),
    path('review-delete/<int:pk>/', ReviewDelete.as_view(), name='review-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
