from django.contrib import admin
from .models import Crop, Market, PriceEntry

admin.site.register(Crop)
admin.site.register(Market)
admin.site.register(PriceEntry)