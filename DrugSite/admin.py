from django.contrib import admin
from .models import Drug, Prescriber, StateData, Triple

# Register your models here.
admin.site.register(Drug)
admin.site.register(Prescriber)
admin.site.register(StateData)
admin.site.register(Triple)