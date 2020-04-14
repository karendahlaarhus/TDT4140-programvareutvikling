# Gruppe 25 - Vaskelister for SiF

Vaskelister er en nettapplikasjon utviklet for Studentsamskipnaden i Fredrikstad.
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
[Git for windows](https://gitforwindows.org).

### Installasjon av forutsetninger

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

### Kjøre applikasjonen

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

4. Oppdater databasen

```bash
python3 manage.py migrate
```

5. Kjør programmet med følgende kommando.

```bash
python3 manage.py runserver
```

Nå kan du besøke nettsiden på localhost:8000, i hvilken som helst nettleser.

## Test applikasjonen

Gruppen har implementert code coverage for å teste prosjektets back-end. Med coverage får
vi testet 90% av koden vår. For å kunne kjøre testene trenger du kun å installere coverage 
med pip. 

For å teste applikasjonen, cd inn i mappen 'SiF' og kjør følgende kommando:

```bash
python manage.py test
```

Om du ønsker å teste én spesifik fil er det bare å legge til filnavnet etter 'test'.

For en mer detaljert rapport om testresultatene, test på følgende måte:

```bash
coverage erase
```

Dette sletter testdatabasen. Cd inn i mappen 'SiF', og Kjør så selve testen med

```bash
coverage run --source="." manage.py test
```

Herfra kan du hente en mer detaljert rapport over alle filene med:

```bash
coverage report
```

Hvis du kun ønsker å se rapporten på visse filer, kan det også gjøres

```bash
coverage report -m --include="Navn på fil 1", "Navn på fil 2", etc
```

### Lisens

MIT © Matega

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom 
the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

