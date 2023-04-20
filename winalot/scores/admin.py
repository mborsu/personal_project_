from django.contrib import admin
from .models import Comment, Team, Tournament, Pool, Match

# Register the Tournament, Team, Pool, and Match models with the admin site
admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Pool)
admin.site.register(Match)


# Specify the CommentAdmin class as the custom admin options for it
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed 
    list_display = ('auteur', 'contenu', 'match', 'date')


