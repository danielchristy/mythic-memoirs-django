from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Character)
admin.site.register(Session)
admin.site.register(Location)
admin.site.register(Event)