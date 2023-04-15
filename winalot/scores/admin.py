from django.contrib import admin

from .models import Team, Tournament

admin.site.register(Tournament)

admin.site.register(Team)