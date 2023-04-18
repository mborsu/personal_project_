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
    


class PoolView(generic.DetailView):
    template_name = 'scores/detail.html'
    
    def get_queryset(self):
        return Tournament.objects.order_by('name')
        
        

