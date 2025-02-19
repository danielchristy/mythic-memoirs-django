from django.urls import path
from . import views

urlpatterns = [
    path('sessions/', views.SessionList.as_view(), name='Session-list'),
    path('sessions/<int:pk>', views.SessionDetail.as_view(), name='session-detail'),
]
