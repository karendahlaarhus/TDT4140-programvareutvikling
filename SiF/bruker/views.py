from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import BrukerForm
from .models import bruker
from vaskelister.models import Vaskeliste
from studentby.models import studentby
from kollektiv.models import kollektiv



class LoginView(TemplateView):
    def get(self, request):
        form = BrukerForm()
        return render(request, 'registration/login.html',{'form': form})
    def post(self, request):
       form = BrukerForm()
       brukernavn_skrevet = request.POST.get('Brukernavn')
       try:
           b = bruker.objects.get(brukernavn=brukernavn_skrevet)
           passord_skrevet = request.POST.get('Passord')
           if passord_skrevet==b.passord:
               if b.isManager:
                   try:
                       correctKollektiv = kollektiv.objects.get(studentby=b.kollektiv.studentby, kollektivNr=b.kollektiv.kollektivNr)
                       url = 'http://127.0.0.1:8000/oversikt/'+str(correctKollektiv.studentby.id)
                       return redirect(url)
                   except studentby.DoesNotExist:
                    return render(request, 'bruker/managerside.html', {'text': "Noe har skjedd feil"}) # 'navn': brukernavn_skrevet, 'manager_for_by':b.kollektiv.studentby,'manager_for_kollektiv':kollektiv, 'vaskeliste_id':b.kollektiv.kollektivNr})
               else:
                   try:
                       vaskeliste = Vaskeliste.objects.get(kollektiv=b.kollektiv)
                       url = 'http://127.0.0.1:8000/vask/'+str(vaskeliste.id)
                       return redirect(url)
                   except Vaskeliste.DoesNotExist:
                       return render(request,'bruker/beboerside.html')
           else:
               return render(request, 'registration/login.html', {'form': form, 'text': 'Ugyldig passord'})
       except bruker.DoesNotExist:
           return render(request, 'registration/login.html', {'form': form, 'text': 'Ugyldig brukernavn'})

