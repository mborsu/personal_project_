from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pool, Tournament, Match, Comment


class IndexView(generic.ListView):
    # Displays a list of all tournaments
    model = Tournament
    template_name = 'scores/index.html'
    context_object_name = 'tournament_list'

    def get_queryset(self):
        return Tournament.objects.order_by('name')


class PoolView(generic.DetailView):
    # Displays the details of a single pool, including all matches
    model = Tournament
    template_name = 'scores/detail.html'
    
    
class MatchView(generic.DetailView):
    # Displays the details of a single match, including comments
    model = Pool
    template_name = 'scores/match_detail.html'
    
    
class CommentView(generic.DetailView):
    # Displays the comments for a single match and allows users to add new comments
    model = Match
    template_name = 'scores/match_comment.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # Retrieve all comments for this match and order them by date
        comments_connected = Comment.objects.filter(match=self.get_object()).order_by('-date')
        data['comments'] = comments_connected
        return data

    def post(self, request, *args, **kwargs):
        # Create a new comment from the POST data and save it to the database
        new_comment = Comment(contenu=request.POST.get('contenu'),
                              auteur=self.request.user,
                              match=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class EditCommentView(LoginRequiredMixin, generic.UpdateView):
    # Allows users to edit their own comments
    model = Comment
    fields = ['contenu']
    template_name = 'scores/edit_comment.html'
    success_url = reverse_lazy('scores:comment')

    def get_success_url(self):
        # Redirect to the comments page for the match that this comment belongs to
        return reverse('scores:comment', args=[self.object.match.pk])
