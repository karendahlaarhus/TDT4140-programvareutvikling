from django.test import TestCase, Client
from vaskelister.models import Vaskeliste, Task
import datetime

class TestVaskelisteView(TestCase):
    def setUp(self):
        self.c = Client()

        self.current_week = int(datetime.datetime.now().strftime("%U")) + 1
        # Vaskeliste fra inneværende uke
        Vaskeliste.objects.create(name="Test1", week=self.current_week)
        self.v1 = Vaskeliste.objects.get(name="Test1")
        Task.objects.create(text="Vaske do", vaskeliste=self.v1)
        Task.objects.create(text="Vaske kjøkken", vaskeliste=self.v1, complete=True)
        self.task1 = Task.objects.get(text="Vaske do", vaskeliste=self.v1)
        self.task2 = Task.objects.get(text="Vaske kjøkken", vaskeliste=self.v1)

        #Vaskeliste fra forrige uke
        Vaskeliste.objects.create(name="Test2", week=self.current_week - 1)
        self.v2 = Vaskeliste.objects.get(name="Test2")
        Task.objects.create(text="Vaske do", vaskeliste=self.v2, complete=True)
        Task.objects.create(text="Vaske kjøkken", vaskeliste=self.v2)
        self.task3 = Task.objects.get(text="Vaske do", vaskeliste=self.v2)
        self.task4 = Task.objects.get(text="Vaske kjøkken", vaskeliste=self.v2)

    def test_currentweek(self):
        # Tester at index view viser riktig liste over Tasks og uke for inneværende uke
        url = '/vask/' + str(self.v1.id)
        response = self.c.get(url)

        # laster inn objektene på nytt tilfelle endring
        self.v1 = Vaskeliste.objects.get(name="Test1")
        self.task1 = Task.objects.get(text="Vaske do", vaskeliste=self.v1)
        self.task2 = Task.objects.get(text="Vaske kjøkken", vaskeliste=self.v1)

        self.assertTemplateUsed(response, 'bruker/beboerside.html')  # bruker riktig template
        self.assertEquals(self.v1.week, response.context['week'])  # viser riktig uke
        task_liste = response.context['todo_list']
        self.assertTrue((len(task_liste) == 2) and (self.task1 in task_liste) and (self.task2 in task_liste))

        #Tester at vaskelisten ikke har blitt noe endret
        self.assertEquals(self.v1.week, self.current_week)
        self.assertFalse(self.task1.complete)
        self.assertTrue(self.task2.complete)

    def test_not_currentweek(self):
        # Tester at index view viser riktig dersom vaskeliste ikke er fra inneværende uke
        url = '/vask/' + str(self.v2.id)
        response = self.c.get(url)

        # laster inn objektene på nytt tilfelle endring
        self.v2 = Vaskeliste.objects.get(name="Test2")
        self.task3 = Task.objects.get(text="Vaske do", vaskeliste=self.v2)
        self.task4 = Task.objects.get(text="Vaske kjøkken", vaskeliste=self.v2)

        self.assertTemplateUsed(response, 'bruker/beboerside.html')  # bruker riktig template
        self.assertEquals(self.v2.week, response.context['week'])  # viser riktig uke
        task_liste = response.context['todo_list']
        self.assertTrue((len(task_liste) == 2) and (self.task3 in task_liste) and (self.task4 in task_liste))

        # Tester at vaskelisten har blitt endret riktig
        #self.assertEquals(self.v2.week, self.current_week) #En vaskelistes uke skal være inneværende uke
        self.assertFalse(self.task3.complete) # Ingen tasks i vaskelisten skal være complete lenger
        self.assertFalse(self.task4.complete)





