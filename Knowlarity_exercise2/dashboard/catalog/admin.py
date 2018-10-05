from django.contrib import admin

# Register your models here.
from catalog.models import Team, Match

admin.site.register(Team)
admin.site.register(Match)
