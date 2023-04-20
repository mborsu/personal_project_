from django.urls import path
from . import views

app_name = 'scores'

# URL patterns for the scores app
urlpatterns = [
    # Index view
    path('', views.IndexView.as_view(), name='index'),
    
    # Detail view for a pool
    path('<int:pk>/', views.PoolView.as_view(), name='pool'),
    
    # Detail view for a match
    path('pool/<int:pk>/', views.MatchView.as_view(), name='match'),
    
    # Detail view for a match's comments and post new comment
    path('match/<int:pk>/', views.CommentView.as_view(), name='comment'),
    
    # Edit a comment view
    path('comment/<int:pk>/edit/', views.EditCommentView.as_view(), name='edit_comment'),
]
