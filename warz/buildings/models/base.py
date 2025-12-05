from django.db import models
from warz.core.models import Village
from warz.core.models import AbstractBaseModel

class BuildingBase(AbstractBaseModel):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)

    base_wood_cost = models.IntegerField(default=100)
    base_stone_cost = models.IntegerField(default=100)
    base_iron_cost = models.IntegerField(default=100)

    class Meta:
        abstract = True