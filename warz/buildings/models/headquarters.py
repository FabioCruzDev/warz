from warz.buildings.models.base import AbstractBuilding
from django.db import models

class Headquarters(AbstractBuilding):
    build_speed_factor = models.FloatField(default=1.0)

    def get_build_time_modifier(self):
        return 1 / (1 + (self.level * 0.05))

    class Meta:
        constraints = [models.UniqueConstraint(fields=['village'], name='unique_headquarters_village')]