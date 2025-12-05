from django.db import models
from warz.core.models.village import Village
from warz.core.models.base import AbstractBaseModel

class AbstractBuilding(AbstractBaseModel):
    # A village may have multiple buildings of the same type, so use ForeignKey
    # Use related_name='+' to avoid creating reverse accessors for each concrete
    # building subclass (prevents name collisions).
    village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='+')
    level = models.IntegerField(default=1)

    base_wood_cost = models.IntegerField(default=100)
    base_stone_cost = models.IntegerField(default=100)
    base_iron_cost = models.IntegerField(default=100)

    class Meta:
        abstract = True