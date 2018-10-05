from django.shortcuts import render

# Create your views here.
from catalog.models import Team, Match

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_teams = Team.objects.all().count()
    num_matches = Match.objects.all().count()

    
    context = {
        'num_teams': num_teams,
        'num_matches': num_matches,
    }

    return render(request, 'index.html', context=context)


from django.views import generic

class TeamListView(generic.ListView):
    model = Team
    # context_object_name = 'my_team_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war


class MatchListView(generic.ListView):
	model = Match

class TopTeams(generic.ListView):
	model = Team


	def get_queryset(self):
		top_scores = (Team.objects.order_by('-points').values_list('points', flat=True).distinct())
		top_records = (Team.objects.order_by('-points').filter(points__in=top_scores[:10]))
		# top_records = Team.objects.all()
		return top_records[:10]

# from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy

# from catalog.models import Match

# class MatchCreate(CreateView):
#     model = Match
#     fields = '__all__'
#     print(Match.winner,"BULLDOGBULLDOG234324334132413784371878")
#     success_url = reverse_lazy('matches')


import datetime

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import NewMatchForm


def NewMatch(request):
    match = Match()
    form = NewMatchForm(request.POST)

    if form.is_valid():
        match = Match()
        team1 = Team()
        team2 = Team()
        # match.serial_num = form.cleaned_data['serial_num']
        team1.player1 = form.cleaned_data["team1_p1"]
        team1.player2 = form.cleaned_data["team1_p2"]
        team2.player1 = form.cleaned_data["team2_p1"]
        team2.player2 = form.cleaned_data["team2_p2"]




        # Now update the teams database
        # if a new team has participated then add it to the database
        t1p1 = team1.player1
        t1p2 = team1.player2
        t2p1 = team2.player1
        t2p2 = team2.player2

        winner = form.cleaned_data["winner"]

        if Team.objects.filter(player1=t1p1, player2=t1p2).exists():
            team = Team.objects.filter(player1 = t1p1 , player2 = t1p2).first()
            team1 =team
            if winner == '1':
            	team1.points +=10
            else:
            	team1.points -=10

            team1.delete()
            team1.save()
        else:
        	# team = Team()
        	# team.player1 = t1p1
        	# team.player2 = t1p2
        	if winner == '1':
        		team1.points +=10
        	else:
        		team1.points -=10

        	team1.save()

        if Team.objects.filter(player1 = t2p1,  player2 =t2p2).exists():
            team = Team.objects.filter(player1 = t2p1,  player2 = t2p2).first()
            team2 = team
            if winner == '2':
                team2.points +=10
            else:
                team2.points -=10

            team2.delete()
            team2.save()
        else:
            # team = Team()
            # team.player1 = t2p1
            # team.player2 = t2p2
            if winner == '2':
              team2.points +=10
            else:
              team2.points -=10

            team2.save()

       

        match.team1 = team1
        match.team2 = team2
        match.winner = form.cleaned_data["winner"]
        match.save()
        return HttpResponseRedirect(reverse("top_teams"))


    context = {
        'form': form,
    }

    return render(request, 'catalog/new_match.html', context)



