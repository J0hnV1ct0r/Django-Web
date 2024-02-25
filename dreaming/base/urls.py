from django.urls import path
from .views import WorkList, WorkDetail, WorkCreate, WorkUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', WorkList.as_view(), name='works'),
    path('work/<int:pk>/', WorkDetail.as_view(), name='work'),
    path('work-create', WorkCreate.as_view(), name='work-create'),
    path('work-update/<int:pk>/', WorkUpdate.as_view(), name='work-update'),
    path('work-delete/<int:pk>/', DeleteView.as_view(), name='work-delete'),
]
