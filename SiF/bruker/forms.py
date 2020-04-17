from django import forms

class BrukerForm(forms.Form):  #form som brukes for innlogging for bruker
    Brukernavn = forms.CharField()
    Passord = forms.CharField(widget=forms.PasswordInput)



