from django.urls import path
from gamefield.views import game_view

urlpatterns = [
    path('game/', game_view, name='game_view'),
    # 他のURLパターンをここに追加する場合もあるかもしれません
]
