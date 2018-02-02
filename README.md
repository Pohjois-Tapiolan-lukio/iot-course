# Kurssimateriaalia: IoT-sovellukset
## Sisällyslettelo
* [Esittely](#esittely)
* [Pakollinen osio](#pakollinen)
  * [Perusteet](#perusteet)
* [Vapaavalintaiset osiot](#vapaavalintaiset)
  * [Arduino ja IoT](#arduino)
  * [SenseHAT-sensorit](#sensehat)
  * [Tiedonsiirto ja analyysi](#iot)

## <a name="esittely"></a>Esittely
Tervetuloa Robotiikka ja IoT-sovellukset -kurssin IoT-osioon.

Tästä dokumentista löydät linkit kurssin IoT-osion
oppimateriaaleihin. On suositeltavaa käydä
[Perusteet-osio](#perusteet) läpi, ja sen jälkeen siirtyä siihen
osioon joka kuulostaa mielenkiintoisimmalta.

Huomio: esimerkkien soveltaminen ja omien (aiheellisten) projektien
toteuttaminen valmiiden projektien sijaan on myös suositeltua.

## <a name="pakollinen"></a>Pakollinen osio
### <a name="perusteet"></a>Perusteet
Tässä osiossa käydään läpi tiedonsiirron perusteet, joka toimii
kaikkien IoT-projektien pohjatietona. Tietoa siirretään Raspberry
Pi-tietokoneesta koulun palvelimelle, jossa tieto säilytetään
mahdollista myöhempää analyysia varten.
1. [Projektin luominen](perusteet-01/)
2. [Tiedonsiirron perusteita](perusteet-02/)
3. [Ensimmäinen taulukko, ensimmäiset datat](perusteet-03/)

[KOMENTORIVI.md](KOMENTORIVI.md) on hyödyllinen resurssi komentoriviin
tutustumisessa.

## <a name="vapaavalintaiset"></a>Vapaavalintaiset osiot
### <a name="arduino"></a>Arduino/ulkoiset sensorit ja IoT
Tässä osiossa on projekteja joissa käytetään
Arduino-mikrokontrollereita datankeräysalustana. Arduinot ovat
pienitehoisia tietokoneita joita yleensä käytetään esimerkiksi LEDien,
nappien, sensorien, tai muun raudan kanssa toimimiseen. *Arduinot ovat
erityisen hyödyllisiä esimerkiksi sellaisten sensorien kanssa, jotka
välittävät datansa analogisesti, sillä Raspberry Pi:n omat pinit ovat
kaikki digitaalisia, kun Arduinoissa on analogisiakin.*
- [Liiketunnistin](https://github.com/Pohjois-Tapiolan-lukio/raspberry_pi-projects/tree/master/hardware_GPIO/liiketunnistin)
- [Ultraääni-sensori](https://github.com/Pohjois-Tapiolan-lukio/raspberry_pi-projects/tree/master/hardware_GPIO/ultraani)
- [Telegram-selfie](https://github.com/Pohjois-Tapiolan-lukio/raspberry_pi-projects/tree/master/picamera)

### <a name="sensehat"></a>SenseHAT-sensorit
Tässä osiossa on projekteja joissa käytetään SenseHAT-lisäosan
sensoreita datan keräämistä ja mahdollisesti esittämistä varten.
SenseHAT on Raspberry Pi:n päälle asetettava "shieldi" jossa on 8x8
LED-näyttö ja paljon ympäristöä tutkivia sensoreja.
- [Ympäristösensorit](https://github.com/Pohjois-Tapiolan-lukio/sensehat-materials/blob/master/iot-sensor/iot_sensor.py)

### <a name="iot"></a>Tiedonsiirto ja analyysi
Tässä osiossa on projekteja jotka keskittyvät hyvin vähän datan
keräämiseen.  Datan keräämisen sijaan tässä perehdytään tarkemmin
tiedonsiirtoon ja erityisesti datan analysointiin Pythonilla.
