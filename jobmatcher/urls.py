from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name="home_page"),
    path('matcher/bestCandidates/', views.getCandidates, name="get_candidates")
]