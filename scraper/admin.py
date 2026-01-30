from django.contrib import admin
from .models import ScrapedData

# Esto hace que tu tabla aparezca en el panel de control
# admin.site.register(ScrapedData)

##Esto registra tu tabla en el panel de administración
@admin.register(ScrapedData)
class ScrapedDataAdmin(admin.ModelAdmin):
    list_display = ('author', 'quote', 'created_at') # Lo que se verá en la lista
    search_fields = ('author', 'quote')              # Barra de búsqueda
