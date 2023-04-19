from django.shortcuts import get_object_or_404, render, redirect
from .models import Pool, Tournament, Match, Commentaire
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



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


class MatchView(generic.DetailView):
    template_name = 'scores/match_detail.html'
    
    def get_queryset(self):
        return Pool.objects.order_by('name')
    
    
class CommentView(generic.DetailView):
    template_name = 'scores/match_comment.html'

    def get_queryset(self):
        return Match.objects.order_by('id')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Commentaire.objects.filter(
            match=self.get_object()).order_by('-date')
        data['comments'] = comments_connected
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Commentaire(contenu=request.POST.get('contenu'),
                                  auteur=self.request.user,  # Utiliser self.request.user pour définir l'auteur
                                  match=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
    
from django.urls import reverse
from django.shortcuts import redirect

from django.shortcuts import redirect
from django.urls import reverse_lazy

class EditCommentView(LoginRequiredMixin, generic.UpdateView):
    model = Commentaire
    fields = ['contenu']
    template_name = 'scores/edit_comment.html'
    success_url = reverse_lazy('scores:comment')

    def get_success_url(self):
        return reverse('scores:comment', args=[self.object.match.pk])
    
    
