from django.urls import path, include
from . import views




urlpatterns = [
    path('signup/',views.UserSignUP.as_view()),
    path('login/', views.LogInView.as_view()),
]
