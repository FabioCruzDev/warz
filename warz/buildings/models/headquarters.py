from warz.buildings.models.base import BuildingBase
from django.db import models

class Headquarters(BuildingBase):
    build_speed_factor = models.FloatField(default=1.0)

    def get_build_time_modifier(self):
        return 1 / (1 + (self.level * 0.05))