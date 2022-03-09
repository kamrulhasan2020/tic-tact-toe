from operator import mod
from django.db import models


class Game(models.Model):
    code = models.CharField(max_length=8, unique=True)
    active = models.BooleanField(default=False)
    player1 = models.CharField(max_length=100, blank=True)
    player2 = models.CharField(max_length=100, blank=True)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    turn = models.CharField(max_length=100, blank=True)


class Board(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='board')
    cell1 = models.CharField(max_length=10, blank=True)
    cell2 = models.CharField(max_length=10, blank=True)
    cell3 = models.CharField(max_length=10, blank=True)
    cell4 = models.CharField(max_length=10, blank=True)
    cell5 = models.CharField(max_length=10, blank=True)
    cell6 = models.CharField(max_length=10, blank=True)
    cell7 = models.CharField(max_length=10, blank=True)
    cell8 = models.CharField(max_length=10, blank=True)
    cell9 = models.CharField(max_length=10, blank=True)
