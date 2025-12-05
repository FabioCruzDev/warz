from django.db import models

from warz.buildings.models.base import AbstractBuilding

class Housing(AbstractBuilding):
    base_population_capacity = models.IntegerField(default=100)

    def get_capacity(self):
        """
        Aumenta o limite de população com base no level.
        Exemplo: +30% por nível.
        """
        factor = 1.3
        return int(self.base_population_capacity * (factor ** (self.level - 1)))

    class Meta:
        constraints = [models.UniqueConstraint(fields=['village'], name='unique_housing_village')]