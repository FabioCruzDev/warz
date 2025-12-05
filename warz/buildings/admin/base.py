from django.contrib import admin

class AbstractBuildingAdmin(admin.ModelAdmin):
    search_fields = ('level', 'village__name', 'village__owner__user__username')
    list_filter = ('level',)