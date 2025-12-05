

from warz.buildings.models.base import AbstractBuilding
from django.db import models


class Stable(AbstractBuilding):
    pass

    class Meta:
        constraints = [models.UniqueConstraint(fields=['village'], name='unique_stable_village')]
