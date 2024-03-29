# users/urls.py
from django.conf.urls import url
from django.urls import path
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView, authenticate_user
app_name = 'users'

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
    path('obtain_token/', authenticate_user),
]
