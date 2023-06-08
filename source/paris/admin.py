from django.contrib import admin
from .models import ParisEtablissement


@admin.register(ParisEtablissement)
class ParisEtablissementAdmin(admin.ModelAdmin):
    
    list_display = ["name","variant","limit","phone"]
    ordering = ["limit"]