from django.urls import path

from . import views

urlpatterns = [
    path("computers/<pk>/", views.RetrieveComputerView.as_view()),
]
