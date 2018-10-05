from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('matches/', views.MatchListView.as_view(), name='matches'),

]

urlpatterns += [   
    # path('matchcreate/', views.MatchCreate.as_view(), name='match_create'),
    path('topteams/', views.TopTeams.as_view(), name='top_teams')
 ]

urlpatterns += [   
    path('newmatch/', views.NewMatch, name='newmatch'),
]