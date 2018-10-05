import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class NewMatchForm(forms.Form):
    # serial_num = forms.IntegerField()
    team1_p1 = forms.CharField(max_length=200)
    team1_p2 = forms.CharField(max_length=200)
    team2_p1 = forms.CharField(max_length=200)
    # t1_m1 = forms.CharField(max_length=200)
    # t1_m2 = forms.CharField(max_length=200)
    team2_p2 = forms.CharField(max_length=200)
    # t2_m1 = forms.CharField(max_length=200)
    # t2_m2 = forms.CharField(max_length=200)

    winner = forms.CharField(max_length=200)

    def clean_winner(self):
        data = self.cleaned_data['winner']
        
        if (data == '1' or data == '2'):
        	return data;

        raise ValidationError(_("winner must be palyer 1 or player 2"))
