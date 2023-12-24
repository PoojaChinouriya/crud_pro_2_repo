from django.urls import path
from .views import UserAPI


urlpatterns = [
    path('user-create/', UserAPI.as_view()),
]