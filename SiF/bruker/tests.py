from django.test import TestCase, Client
from bruker.models import bruker
from studentby.models import studentby
from kollektiv.models import kollektiv
from vaskelister.models import Vaskeliste, Task

class TestBrukerView(TestCase):
    def setUp(self):
        #setUp-metoden kjører før hver test
        self.c = Client()

        studentby.objects.create(navn="Test", adresse="Testeveien")
        self.s = studentby.objects.get(navn="Test")
        Vaskeliste.objects.create(name="Test")
        self.v = Vaskeliste.objects.get(name="Test")
        kollektiv.objects.create(kollektivNr=1, studentby=self.s, vaskeliste=self.v)
        kollektiv.objects.create(kollektivNr=2, studentby=self.s)
        k1 = kollektiv.objects.get(kollektivNr=1, studentby=self.s) #kollektiv med vaskeliste
        k2 = kollektiv.objects.get(kollektivNr=2, studentby=self.s) #kollektiv uten vaskeliste
        bruker.objects.create(brukernavn="testmanager", passord="passord123", isManager=True, kollektiv=k1) #manager
        bruker.objects.create(brukernavn="testbeboer1", passord="passord123", isManager=False, kollektiv=k1) #vanlig beboer
        bruker.objects.create(brukernavn="testbeboer2", passord="passord123", isManager=False, kollektiv=k2) #beboer uten tilknyttet vaskeliste

    def test_wrong_username(self):
        #Når man skriver inn feil brukernavn, skal man få opp beskrivende tekst på siden
        response = self.c.post('/login/', {'Brukernavn': 'feil', 'Passord': 'passord123'}, follow=True)
        self.assertTemplateUsed(response, 'registration/login.html') #test at view renders riktig template
        self.assertContains(response, 'Ugyldig brukernavn') #test at you man får opp teksten med Ugyldig brukernavn

    def test_wrong_password(self):
        # Når man skriver inn feil passord, skal man få opp beskrivende tekst på siden
        response = self.c.post('/login/', {'Brukernavn': 'testbeboer1', 'Passord': 'feil'}, follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')  # test at view renders riktig template
        self.assertContains(response, 'Ugyldig passord')  # test at man får opp teksten med Ugyldig passord

    def test_ismanager(self):
        # Når man logger inn som manager skal man redirectes til riktig url
        response = self.c.post('/login/', {'Brukernavn': 'testmanager', 'Passord': 'passord123'}, follow=True)
        url = 'http://127.0.0.1:8000/oversikt/' + str(self.s.id)
        self.assertRedirects(response, url)

    def test_notmanager(self):
        # Når man logger inn som bebeoer skal man redirectes til riktig url
        response = self.c.post('/login/', {'Brukernavn': 'testbeboer1', 'Passord': 'passord123'}, follow=True)
        url = 'http://127.0.0.1:8000/vask/' + str(self.v.id)
        self.assertRedirects(response, url)

    def test_no_vaskeliste(self):
        # Setup - bruker uten vaskeliste

        # Dersom man logger inn med bruker uten tilknyttet vaskeliste skal man få opp passende tekst
        response = self.c.post('/login/', {'Brukernavn': 'testbeboer2', 'Passord': 'passord123'}, follow=True)
        self.assertTemplateUsed(response, 'bruker/beboerside.html')  # test at view renders riktig template
        self.assertContains(response, 'ingen tilknyttet vaskeliste')  # test at you man får opp passende tekst








