from django.test import TestCase, Client
from bruker.models import bruker
from studentby.models import studentby
from kollektiv.models import kollektiv



class TestStudentbyView(TestCase):
    def test_index_view(self):
        #setup:
        studentby.objects.create(navn="Test", adresse="Testeveien")
        s = studentby.objects.get(navn="Test")
        kollektiv.objects.create(kollektivNr=1, studentby=s)
        kollektiv.objects.create(kollektivNr=2, studentby=s)
        k1 = kollektiv.objects.get(kollektivNr=1, studentby=s)
        k2 = kollektiv.objects.get(kollektivNr=2, studentby=s)
        bruker.objects.create(brukernavn="manager1", passord="passord", isManager=True, kollektiv=k1)

        c = Client()

        #tester at studentbyIndex gir riktig studentby og liste over kollektiv
        url = '/oversikt/'+str(s.id)
        response = c.get(url)
        self.assertTemplateUsed(response, 'bruker/managerside.html') #bruker riktig template
        self.assertEquals(s, response.context['manager_for_by']) #studentbyIndex gir riktig Studentby
        kollektiv_liste = response.context['kollektiv_list']
        self.assertTrue((len(kollektiv_liste) == 2) and (k1 in kollektiv_liste) and (k2 in kollektiv_liste)) #studentbyIndex gir riktig kollektiv







