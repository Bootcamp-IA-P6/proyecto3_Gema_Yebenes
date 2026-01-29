from django.contrib import admin
from .models import ScrapedData

# Esto hace que tu tabla aparezca en el panel de control
admin.site.register(ScrapedData)
