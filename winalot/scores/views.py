from django.shortcuts import render
from .models import Tournament, Match
from django.views import generic



class IndexView(generic.ListView):
    template_name = 'scores/index.html'
    model = Tournament
    context_object_name = 'tournament_list'

    def get_queryset(self):
        """Return all the tournaments"""
        tournaments =  Tournament.objects.order_by('name')
        print (f"tournaments={tournaments}")
        return tournaments
    
class DetailView(generic.DetailView):
    template_name = 'scores/detail.html'
    
    def get_queryset(self):
        """
        get details of the tournament
        """
        return Tournament.objects

def detail_tournament(request, tournament_id):
    # Récupération du tournoi correspondant à l'ID donné
    tournament = Tournament.objects.get(id=tournament_id)
    # Récupération de tous les matchs associés à ce tournoi
    matchs = Match.objects.filter(tournament=tournament)
    # Création d'un dictionnaire pour passer les données à la vue
    context = {
        'tournament': tournament,
        'matchs': matchs,
    }
    # Rendu de la vue avec les données
    return render(request, 'detail.html', context)

