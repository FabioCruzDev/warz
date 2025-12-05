from django.contrib import admin
from warz.core.models.village import Village

# Register your models here.
@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    pass