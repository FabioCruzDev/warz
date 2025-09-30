from django.contrib import admin
from warz.player.models import Player

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'is_vip')
    search_fields = ('user__username',)
    list_filter = ('is_vip',)
