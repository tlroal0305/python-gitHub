from django.urls import path
from board.views import board
from user.views import singin
from user.views import singup

urlpatterns = [
    path("", board, name="board"),
    path("user/singin", singin, name="singin"),
    path("user/singup", singup, name="singup"),
]