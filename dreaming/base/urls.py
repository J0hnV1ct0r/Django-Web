from django.urls import path
from .views import WorkList, WorkDetail, WorkCreate

urlpatterns = [
    path('', WorkList.as_view(), name='works'),
    path('work/<int:pk>/', WorkDetail.as_view(), name='work'),
    path('work-create', WorkCreate.as_view(), name='work-create'),
]
