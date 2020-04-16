# Gruppe 25 - Vaskelister for SiF  

Vaskelister er en nettapplikasjon utviklet for Studentsamskipnaden i Fredrikstad.
Vi fikk i oppdrag å utvikle en applikasjon som kan la eierne av en studentby holde oversikt
over deres beboere, og hvor godt de utfører sine vaskeoppgaver.

## Motivasjon

Produktet ble utviklet for faget TDT4140 - Programvareutvikling. I dette faget opptrer en studentassistent
som kunde, i dette tilfellet CEO for Studentsamskipnaden i Fredrikstad. Gruppen har i oppgave å utvikle et
produkt for denne kunden. 

## Rammeverk

Nettapplikasjonen er utviklet med Django, et Web-rammeverk skrevet i Python.
DBMSen vår er SQLite. Prosjektets front-end er utviklet kun med HTML og CSS.

## Kodestandard

Gruppen følger [PEP-8 standarden](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjrga2Uh-joAhUJ0aYKHTinAhkQFjAAegQIAxAB&url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0008%2F&usg=AOvVaw0xCyNbAyoecmbLoILApdrP)
for Python.

## Screenshots

<img src="https://www.picturepaste.ca/images/2020/04/15/Skjermbilde-2020-04-15-kl.-16.25.01.png" width=600 height=340>

<br/><br/>

<img src="https://www.picturepaste.ca/images/2020/04/15/Skjermbilde-2020-04-15-kl.-12.05.54.png" width=600 height=340>

<br/><br/>

<img src="https://www.picturepaste.ca/images/2020/04/15/Skjermbilde-2020-04-15-kl.-11.59.02.png" width=600 height=340>

<br/><br/>

<img src="https://www.picturepaste.ca/images/2020/04/15/Skjermbilde-2020-04-15-kl.-12.08.30.png" width=600 height=340>



Bilde 1: Forside

Bilde 2: Login

Bilde 3: Beboerside med vaskeliste

Bilde 4: Eksempelfunksjonalitet fra admins perspektiv

## Komme i gang

Pass på at du har installert [Python 3.7](https://www.python.org/downloads/) med nyeste versjon av [pip](https://pip.pypa.io/en/stable/installing/#upgrading-pip). 
Med pip installert kan du lett installere django i terminalen med 

```bash
pip install django
```

Sjekk også at du har Git installert med 

```bash
git --version
```
### Installere applikasjonen

Følg disse instruksene for å kjøre applikasjonen lokalt.

1. Klon vårt Git Repo fra terminalen

```bash
git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/25.git
```

2. Cd inn i prosjekt-mappen 

```bash
cd 25
cd SiF
```

3. Skap og aktiver et virtual environment

```bash
virtualenv venv
. source/bin/activate
```

4. Oppdater databasen

```bash
python3 manage.py migrate
```

5. Kjør programmet med følgende kommando

```bash
python3 manage.py runserver
```

Nå kan du besøke nettsiden på localhost:8000, i hvilken som helst nettleser.

PS: Om python3 skaper problemer, prøv de samme kommandoene med 'python' istedet.

6. For å kunne ta i bruk applikasjonen må du lage en admin-bruker med 'createsuperuser'

```bash
python3 manage.py createsuperuser
```

Fyll inn ønsket brukernavn og passord. Dette blir din admin-login.

## Test applikasjonen

Gruppen har implementert code coverage for å se testdekningen for prosjektet. 

```bash
pip install Coverage
```

For å teste applikasjonen, cd inn i mappen 'SiF' og kjør følgende kommando

```bash
python3 manage.py test
```

Om du ønsker å teste én spesifik fil er det bare å legge til filnavnet etter 'test'

For en mer detaljert rapport om testresultatene, test på følgende måte

```bash
coverage erase
```

Dette sletter testdatabasen. Cd inn i mappen 'SiF', og Kjør så selve testen med

```bash
coverage run --source="." manage.py test
```

Herfra kan du hente en mer detaljert rapport over alle filene med

```bash
coverage report
```

Hvis du kun ønsker å se rapporten på visse filer, kan det også gjøres

```bash
coverage report -m --include="Navn på fil 1", "Navn på fil 2", etc
```

## Lisens
Copyright (c) 2020 TDT4140 Gruppe 25

Dette prosjektet bruker [MIT](LICENSE.txt) Lisens 

