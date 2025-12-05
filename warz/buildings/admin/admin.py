from django.contrib import admin
from warz.buildings.admin.base import AbstractBuildingAdmin

from warz.buildings.models import *

@admin.register(Barracks)
class BarracksAdmin(AbstractBuildingAdmin):
    pass

@admin.register(Housing)
class HousingAdmin(AbstractBuildingAdmin):
    pass

@admin.register(Headquarters)
class HeadquartersAdmin(AbstractBuildingAdmin):
    pass

@admin.register(Stable)
class StableAdmin(AbstractBuildingAdmin):
    pass
    
@admin.register(Wall)
class WallAdmin(AbstractBuildingAdmin):
    pass

@admin.register(Watchtower)
class WatchtowerAdmin(AbstractBuildingAdmin):
    pass

@admin.register(Academy)
class AcademyAdmin(AbstractBuildingAdmin):
    pass

@admin.register(ClayFarm)
class ClayFarmAdmin(AbstractBuildingAdmin):
    pass

@admin.register(Farm)
class FarmAdmin(AbstractBuildingAdmin):
    pass

@admin.register(IronMine)
class IronMineAdmin(AbstractBuildingAdmin):
    pass

@admin.register(LumberMill)
class LumberMillAdmin(AbstractBuildingAdmin):
    pass

@admin.register(Quarry)
class QuarryAdmin(AbstractBuildingAdmin):
    pass

@admin.register(Granary)
class GranaryAdmin(AbstractBuildingAdmin):
    pass

@admin.register(Market)
class MarketAdmin(AbstractBuildingAdmin):
    pass

@admin.register(Warehouse)
class WarehouseAdmin(AbstractBuildingAdmin):
    pass


