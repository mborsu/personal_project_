from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    num_pools = models.PositiveIntegerField()
    num_teams_per_pool = models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Pool(models.Model):
    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    coach_name = models.CharField(max_length=255)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name='teams')
    members = models.TextField()
    
    def get_member(self):
        return self.members.split(',')
    def __str__(self):
        return self.name
    def add_member(self, member_name):
        members = self.get_member()
        members.append(member_name)
        self.members = ','.join(members)
        self.save()
    def remove_member(self, member_name):
        members = self.get_players()
        if member_name in members:
            members.remove(member_name)
            self.members = ','.join(members)
            self.save()   
    def __str__(self):
        return self.name

class Match(models.Model):
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    home_score = models.PositiveIntegerField(null=True, blank=True)
    away_score = models.PositiveIntegerField(null=True, blank=True)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)
