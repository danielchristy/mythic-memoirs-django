from django.urls import path
from . import views

urlpatterns = [
    path('sessions/', views.SessionList.as_view(), name='Session-list'),
    path('sessions/<int:pk>', views.SessionDetail.as_view(), name='session-detail'),
    path('characters/', views.CharactersList.as_view(), name='Character-list'),
    path('characters/<int:pk>', views.CharacterDetail.as_view(), name='Character-detail'),
    path('locations/', views.LocationList.as_view(), name='Location-list'),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name='Location-detail'),
]
