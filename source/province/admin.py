from django.contrib import admin
from .models import ProvinceEtablissement

  
@admin.register(ProvinceEtablissement)
class ProvinceEtablissementAdmin(admin.ModelAdmin):
    
    list_display = ["name","variant","limit","phone"]
    ordering = ["limit"]
