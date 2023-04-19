from django.contrib import admin

from .models import Commentaire, Team, Tournament, Pool, Match

admin.site.register(Tournament)

admin.site.register(Team)

admin.site.register(Pool)

admin.site.register(Match)


@admin.register(Commentaire)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'contenu', 'match', 'date')
    search_fields = ('auteur', 'contenu')


