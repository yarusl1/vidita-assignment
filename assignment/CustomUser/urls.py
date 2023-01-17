from django.urls import path
from .views import SignupView, LoginView, AuthTest

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('auth-test/', AuthTest.as_view(), name='auth-test'),
]
