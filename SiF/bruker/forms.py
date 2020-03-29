from django import forms

class BrukerForm(forms.Form):
    Brukernavn = forms.CharField()
    Passord = forms.CharField(widget=forms.PasswordInput)



