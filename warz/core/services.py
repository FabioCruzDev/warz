# game_core/services/village_service.py
from buildings.models.resources.clay_farm import ClayFarm
from buildings.models.resources.lumbermill import LumberMill
from buildings.models.resources.quarry import Quarry
from warz.buildings.models.combat.house import Housing
from warz.buildings.models.headquarters import Headquarters
from warz.buildings.models.resources.farm import Farm
from warz.buildings.models.stocks.granary import Granary
from warz.buildings.models.stocks.warehouse import Warehouse
from warz.core.models import Village

class VillageService:

    @staticmethod
    def create_initial_player_village(owner, name):
        village = Village.objects.create(owner=owner, name=name)

        # Cria buildings iniciais
        Headquarters.objects.create(village=village)
        Housing.objects.create(village=village)
        Quarry.objects.create(village=village)
        LumberMill.objects.create(village=village)
        ClayFarm.objects.create(village=village)
        Warehouse.objects.create(village=village)
        Granary.objects.create(village=village)
        Farm.objects.create(village=village)

        return village