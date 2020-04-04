# Gruppe 25 - Vaskeoversikten

Vaskeoversikten er en nettapplikasjon utviklet for Studentsamskipnaden i Fredrikstad.
Vi fikk i oppdrag å utvikle en applikasjon som kan la eierne av en studentby holde oversikt
over deres beboere, og hvor godt de utfører sine vaskeoppgaver.

## Motivasjon

Produktet ble utviklet for faget TDT4140 - Programvareutvikling. I dette faget skal en Stud.Ass
opptre som kunde, i dette tilfellet CEO for Studentsamskipnaden i Fredrikstad, og gruppen skal utvikle et
produkt for denne kunden. 

## Rammeverk

Nettapplikasjonen er utviklet med Django, et Web-rammeverk skrevet i Python.
DBMSen vår er SQLite. Prosjektets front-end er utviklet kun med HTML og CSS.

## Komme i gang

For å kunne kjøre applikasjonen lokalt trenger du Git, Python versjon 3.6+, og Django installert på din enhet. Følgende
beskrivelse av installasjon antar at enheten kjører på Linux/Mac OS. Hvis din enhet bruker Windows, anbefaler vi at du laster ned 
[Git for windows](https://gitforwindows.org)

##Installasjon av forutsetninger

Hvis du allerede har installert kravene nevnt ovenfor, kan du hoppe til 'kjøre applikasjonen'.

1. For å installere Python, skriv følgende inne i terminalen:

```bash
 sudo apt-get intall python
```

2. På MacOS kan du installere Git med følgende kommando

```bash
git --version
```

3. Og pip kan lett installeres med 

```bash
sudo easy-install pip
```

4. Til slutt må man ha Django.

```bash
sudo pip install django
```

###Kjøre applikasjonen

Følg disse instruksene for å kunne kjøre applikasjonen på din maskin.

1. Klon vårt Git Repo fra terminalen

```bash
git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/25.git
```

2. Gå inn i prosjekt-mappen 

```bash
cd 25
cd SiF
```

3. Skap og aktiver et virtual environment

```bash
virtualenv venv
. source/bin/activate
```

4. Oppdater databasen med

```bash
python3 manage.py migrate
```

5. Kjør programmet

```bash
python3 manage.py runserver
```

Så kan du besøke nettsiden på localhost:8000, i hvilken som helst nettleser.
