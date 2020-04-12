from django.test import TestCase, Client
from bruker.models import bruker
from studentby.models import studentby
from kollektiv.models import kollektiv

class TestBrukerView(TestCase):
    def setUp(self):
        #setUp metoden kjører før hver test
        self.c = Client()

        studentby.objects.create(navn="Test", adresse="Testeveien")
        self.s = studentby.objects.get(navn="Test")
        kollektiv.objects.create(kollektivNr=1, studentby=self.s)
        kollektiv.objects.create(kollektivNr=2, studentby=self.s)
        self.k1 = kollektiv.objects.get(kollektivNr=1, studentby=self.s)
        self.k2 = kollektiv.objects.get(kollektivNr=2, studentby=self.s)
        bruker.objects.create(brukernavn="testmanager", passord="passord123", isManager=True, kollektiv=self.k1)
        bruker.objects.create(brukernavn="testbeboer", passord="passord123", isManager=False, kollektiv=self.k2)


    def test_wrong_username(self):
        #Når man skriver inn feil brukernavn, skal man få opp beskrivende tekst på siden
        response = self.c.post('/login/', {'Brukernavn': 'feil', 'Passord': 'passord123'}, follow=True)
        self.assertTemplateUsed(response, 'registration/login.html') #test at view renders riktig template
        self.assertContains(response, 'Ugyldig brukernavn') #test at you man får opp teksten med Ugyldig brukernavn

    def test_wrong_password(self):
        # Når man skriver inn feil passord, skal man få opp beskrivende tekst på siden
        response = self.c.post('/login/', {'Brukernavn': 'testbeboer', 'Passord': 'feil'}, follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')  # test at view renders riktig template
        self.assertContains(response, 'Ugyldig passord')  # test at man får opp teksten med Ugyldig passord



