from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import BrukerForm
from .models import bruker
from vaskelister.models import Vaskeliste
from vaskelister.views import index as todoIndex

class LoginView(TemplateView):
    def get(self, request):
        form = BrukerForm()
        return render(request, 'registration/login.html',{'form': form})
    def post(self, request):
       form = BrukerForm(request.POST)
       #brukernavn_skrevet = form.fields['Brukernavn'] Dette funket ikke av en eller annen grunn
       brukernavn_skrevet = request.POST.get('Brukernavn')
       try:
           b = bruker.objects.get(brukernavn=brukernavn_skrevet)
           passord_skrevet = request.POST.get('Passord')
           if passord_skrevet==b.passord:
               if b.isManager:
                   return render(request, 'bruker/managerside.html', {'text': "Velkommen til managersiden", 'navn': brukernavn_skrevet, 'manager_for_by':b.kollektiv.studentby,'manager_for_kollektiv':b.kollektiv, 'vaskeliste_id':b.kollektiv.kollektivNr})
               else:
                   kollektiv = b.kollektiv
                   try:
                       vaskeliste = Vaskeliste.objects.get(kollektiv=kollektiv)
                       url = 'http://127.0.0.1:8000/vask/'+str(vaskeliste.id)
                       return redirect(url)
                   except vaskeliste.DoesNotExist:
                       return render(request,'bruker/beboerside.html',{'text': "Velkommen til beboersiden",'navn': brukernavn_skrevet,'kollektiv': kollektiv})
           else:
               return render(request, 'registration/login.html', {'form': form, 'text': 'Ugyldig passord'})
       except bruker.DoesNotExist:
           form = BrukerForm()
           return render(request, 'registration/login.html', {'form': form, 'text': 'Ugyldig brukernavn'})






