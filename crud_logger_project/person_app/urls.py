from django.urls import path
from .views import person_detail, PersonAPI

urlpatterns = [
    path('personApi/', PersonAPI.as_view()),
    path('person-retrive/<int:pk>/',person_detail.as_view()),
]
