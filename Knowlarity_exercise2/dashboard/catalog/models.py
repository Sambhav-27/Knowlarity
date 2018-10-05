from django.db import models

class Team(models.Model):
    # title = models.CharField(max_length=200)

    # rank = models.IntegerField(default=999)
    player1 = models.TextField(max_length=100, help_text='Enter Player 1 name')
    player2 = models.TextField(max_length=100, help_text='Enter Player 2 name')
    points = models.IntegerField(default=0)

    
    
    def __str__(self):
        return self.player1
    
    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this team."""
    #     # return reverse('team-detail', args=[str(self.id)])
    #     return HttpResponseRedirect(reverse('matches-catalog') )


class Match(models.Model):
    # serial_num= models.IntegerField()

    # team3= models.CharField(max_length=200)
    # team4 = models.CharField(max_length=200)
    team1 = models.ForeignKey(Team, related_name="Default_team1", on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name="Default_team2", on_delete=models.CASCADE)
    winner = models.CharField(max_length=200)


	# def get_absolute_url(self):
	# 	return HttpResponseRedirect()




