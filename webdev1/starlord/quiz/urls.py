from django.urls import path
from . import views
import accounts

urlpatterns = [
    path('quiz', views.quiz ,name="quiz"),
    path('login', accounts.views.login ,name="login" ) 
]