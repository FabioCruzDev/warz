

from warz.buildings.models.base import AbstractBuilding
from django.db import models


class Barracks(AbstractBuilding):
    pass

    class Meta:
        constraints = [models.UniqueConstraint(fields=['village'], name='unique_barracks_village')]