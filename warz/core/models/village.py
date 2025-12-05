from django.db import models
from warz.core.models.base import AbstractBaseModel


class Village(AbstractBaseModel):
    player = models.ForeignKey('player.Player', null=True, blank=True, on_delete=models.DO_NOTHING)
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return f"{self.name()} ({self.x}|{self.y})"
    
    def name(self):
        return f"Village of {self.player.user.username}" if self.player else "Barbarian Village"
    
    def coordinates(self):
        return f"({self.x}|{self.y})"
    
    def population(self):
        pass

