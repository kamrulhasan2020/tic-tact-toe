from django.urls import path
from .import views

app_name='main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('game/<str:code>/', views.GameView.as_view(), name='game'),
    path('new-game/', views.new_game, name='new_game'),
    path('join-with-code/', views.join_with_code, name='join_with_code'),
    path('set-name/', views.set_name, name='set_name'),
]