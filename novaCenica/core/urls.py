from django.urls import path
from .views import HomeView, TubeView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('tube_cenica/', TubeView.as_view(), name='TubeCenica'),
]
