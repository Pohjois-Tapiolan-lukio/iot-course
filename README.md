# Kurssimateriaalia: IoT-sovellukset
Tervetuloa Robotiikka ja IoT-sovellukset -kurssin IoT-osioon.

Tästä dokumentista löydät materiaalit jonkin ohjattuun oppimiseen.
On suositeltavaa käydä [Perusteet-osio](#perusteet) läpi, ja sen jälkeen
siirtyä siihen osioon joka kuulostaa mielenkiintoisimmalta.

Huomio: esimerkkien soveltaminen ja omien (aiheellisten) projektien
toteuttaminen valmiiden projektien sijaan on myös suositeltua.

## Pakollinen osio
### Perusteet
Tässä osiossa käydään läpi tiedonsiirron perusteet, joka toimii kaikkien
IoT-projektien pohjatietona. Tietoa siirretään Raspberry Pi-tietokoneesta
koulun palvelimelle, jossa tieto säilytetään mahdollista myöhempää
analyysia varten.
1. [Projektin luominen](perusteet-01/)
2. [Tiedonsiirron perusteita](perusteet-02/)
3. [Ensimmäinen taulukko, ensimmäiset datat](perusteet-03/)
4. [Ensimmäinen käytännön IoT-sovellus](perusteet-04/)

## Vapaavalintaiset osiot
### Arduino ja IoT
Tässä osiossa on projekteja joissa käytetään Arduino-mikrokontrollereita
datankeräysalustana. Arduinot ovat pienitehoisia tietokoneita joita yleensä
käytetään esimerkiksi LEDien, nappien, sensorien, tai muun raudan kanssa
toimimiseen. *Arduinot ovat erityisen hyödyllisiä esimerkiksi sellaisten
sensorien kanssa, jotka välittävät datansa analogisesti, sillä Raspberry Pi:n
omat pinit ovat kaikki digitaalisia, kun Arduinoissa on analogisiakin.*

### SenseHAT-sensorit
Tässä osiossa on projekteja joissa käytetään SenseHAT-lisäosan sensoreita
datan keräämistä ja mahdollisesti esittämistä varten.
SenseHAT on Raspberry Pi:n päälle asetettava "shieldi" jossa on 8x8 LED-näyttö
ja paljon ympäristöä tutkivia sensoreja.

### Tiedonsiirto ja analyysi
Tässä osiossa on projekteja jotka keskittyvät hyvin vähän datan keräämiseen.
Datan keräämisen sijaan tässä perehdytään tarkemmin tiedonsiirtoon ja
erityisesti datan analysointiin Pythonilla.
