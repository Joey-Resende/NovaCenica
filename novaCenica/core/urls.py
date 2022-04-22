from django.urls import path
from .views import HomeView, TubeView, DetailVideoView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('tube_cenica/', TubeView.as_view(), name='TubeCenica'),
    path('o_ator_geek/', DetailVideoView.as_view(), name='o_ator_geek'),
]
