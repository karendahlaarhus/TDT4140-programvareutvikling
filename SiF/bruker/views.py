from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import BrukerForm
from .models import bruker

class LoginView(TemplateView):
    def get(self, request):
        form = BrukerForm()
        return render(request, 'bruker/login.html',{'form': form})
    def post(self, request):
       form = BrukerForm(request.POST)
       #brukernavn_skrevet = form.fields['Brukernavn'] Dette funket ikke av en eller annen grunn
       brukernavn_skrevet = request.POST.get('Brukernavn')
       try:
           b = bruker.objects.get(brukernavn=brukernavn_skrevet)
           passord_skrevet = request.POST.get('Passord')
           if passord_skrevet==b.passord:
               if b.isManager:
                   return render(request, 'bruker/managerside.html', {'text': "Velkommen til managersiden", 'navn': brukernavn_skrevet})
               else:
                   kollektiv = b.kollektiv
                   return render(request, 'bruker/beboerside.html', {'text': "Velkommen til beboersiden", 'navn': brukernavn_skrevet, 'kollektiv': kollektiv})
           else:
               return render(request, 'bruker/login.html', {'form': form, 'text': 'Ugyldig passord'})
       except bruker.DoesNotExist:
           form = BrukerForm()
           return render(request, 'bruker/login.html', {'form': form, 'text': 'Ugyldig brukernavn'})






