from django.db import models
from django.contrib.auth.models import User

# Represents a tournament
class Tournament(models.Model):
    name = models.CharField(max_length=255)                   # Name of the tournament
    location = models.CharField(max_length=255, blank=True)   # Location of the tournament
    start_date = models.DateTimeField(null=True, blank=True)  # Start date of the tournament
    end_date = models.DateTimeField(null=True, blank=True)    # End date of the tournament
    num_pools = models.PositiveIntegerField()                 # Number of pools in the tournament
    num_teams_per_pool = models.PositiveIntegerField()        # Number of teams per pool in the tournament

    def __str__(self):
        return self.name


# Represents a pool within a tournament
class Pool(models.Model):
    name = models.CharField(max_length=255)            # Name of the pool
    number = models.PositiveIntegerField()             # Number of the pool
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)  # Tournament that this pool belongs to

    def __str__(self):
        return self.name


# Represents a team in a pool
class Team(models.Model):
    name = models.CharField(max_length=255)           # Name of the team
    coach_name = models.CharField(max_length=255)     # Name of the coach
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name='teams') # Pool that this team belongs to
    members = models.TextField()                      # Members of the team

    # Return a list of members
    def get_members(self):
        return self.members.split(',')

    def __str__(self):
        return self.name

    # Add a member to the team
    def add_member(self, member_name):
        members = self.get_members()
        members.append(member_name)
        self.members = ','.join(members)
        self.save()

    # Remove a member from the team
    def remove_member(self, member_name):
        members = self.get_members()
        if member_name in members:
            members.remove(member_name)
            self.members = ','.join(members)
            self.save()

    def __str__(self):
        return self.name


# Represents a match between two teams
class Match(models.Model):
    date_time = models.DateTimeField()                
    location = models.CharField(max_length=255)         
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches') 
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches') 
    home_score = models.PositiveIntegerField(null=True, blank=True)  
    away_score = models.PositiveIntegerField(null=True, blank=True) 
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE, null=True) 
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True) 


# Represents a comment on a match
class Comment(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)   
    contenu = models.TextField()                                
    date = models.DateTimeField(auto_now_add=True)               
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return 'Commentaire {} par {}'.format(self.contenu, self.auteur)