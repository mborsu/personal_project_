from django.contrib import admin

from .models import Team, Tournament, Pool, Match, Player

admin.site.register(Tournament)

admin.site.register(Team)

admin.site.register(Pool)

admin.site.register(Match)

admin.site.register(Player)