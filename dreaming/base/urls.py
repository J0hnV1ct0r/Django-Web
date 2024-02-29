from django.urls import path
from .views import (WorkList, WorkDetail, WorkCreate, WorkUpdate, DeleteView, CustomLoginView, RegisterPage,
                    ChallengeList, ChallengeDetail, ChallengeCreate, ChallengeUpdate, ChallengeDelete)
from django.contrib.auth.views import LogoutView

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
]
