from django.contrib import admin

from .models import Plant, Tag, Zone, LocalPlant, Cultivar
admin.site.register(Plant)
admin.site.register(Tag)
admin.site.register(Zone)
admin.site.register(LocalPlant)
admin.site.register(Cultivar)

# Register your models here.
