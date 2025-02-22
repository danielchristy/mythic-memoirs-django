from django.urls import path
from .views import *

urlpatterns = [
    path('sessions/', SessionList.as_view()),
    path('sessions/<int:pk>', SessionDetail.as_view(), name='session-detail'),
    path('characters/', CharacterList.as_view(), name='Character-list'),
    path('characters/<int:pk>', CharacterDetail.as_view(), name='Character-detail'),
    path('locations/', LocationList.as_view(), name='Location-list'),
    path('locations/<int:pk>', LocationDetail.as_view(), name='Location-detail'),
    path('auth/login', LoginView.as_view()),
    path('register', SignupView.as_view()),
    path('csrf_cookie', setCSRFCookie.as_view()),
    path('authenticated', CheckAuthenticatedView.as_view()),
    path('logout', LogoutView.as_view()),
    path('login', LoginView.as_view()),
    path('delete', DeleteAccountView.as_view())
]


