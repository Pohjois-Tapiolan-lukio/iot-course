# Tiedonsiirron perusteita
Perusteet-tehtävissä 2 ja 3 luodaan pienimuotoinen demo jossa
siirretään tietoa Raspberry Pi:stä palvelimelle. Tässä ensimmäisessä
osassa luodaan Git-repository ja tutkitaan tietoliikenteen toimintaa
Pythonissa requests-kirjaston avulla.

### Valmistelut
Luo uusi Git-repo nimeltä "heippa-internet" ja kloonaa se `iot-kurssi`
hakemistoosi. Mikäli et muista miten tämä tapahtuu, voit luntata
[tehtävästä 1](../perusteet-01/). Kaikki koodi tässä tehtävässä ja
seuraavassa menee yhteen tiedostoon, joten luo vielä tiedosto
`main.py`.

Jotta voisimme ottaa ollenkaan yhteyttä koulun palvelimeen, pitää yksi
tärkeä asia varmistaa. Palvelimeen saa yhteyden vain espoo_oppilas
verkon kautta, joten varmista että Raspberrysi on siinä verkossa.

### Requests-kirjasto
Kun ohjelmamme alkaa, haluamme ensimmäisenä importtaa
requests-[kirjaston](#kirjasto), sillä käytämme sitä kaikkeen mitä nyt teemme.

```python
import requests
```

Requests-kirjasto ei vaadi minkäänlaista valmistelua, joten voimme
jatkaa heti itse asiaan.

### Heippa, palvelin!
Ensimmäisenä tehdään vain yksinkertainen [pyyntö](#request) palvelimelle, ja
katsotaan mitä sieltä tulee.

Requests-kirjasto antaa meille funktion `requests.get("<osoite>")` jolla voimme
lähettää pyyntöjä mihin tahansa osoitteeseen. Tämä funktio palauttaa
[palvelimen](#server) vastauksen. Vastaus (`response`-muuttuja) ei 
ole kuitenkaan suoraan tekstimuodossa, mutta saamme sen tekstimuotoon 
hakemalla `text`in `response`-muuttujan sisältä (`response.text` siis 
palauttaa vastauksen tekstimuodossa).

```python
response = requests.get("http://iot.olarinlukio.fi:5000/heippa")
print(response.text)
```

Tämän koodin pitäisi tulostaa "Moikka!", sillä koulun IoT-palvelin on
ohjelmoitu vastaamaan "Moikka!" kun sille lähetetään kutsu joka loppuu
`/heippa`.

---
### Hieman termistöä
#### <a name="kirjasto"></a>Kirjasto
Ohjelmoinnissa "kirjastolla" viitataan valmiiksi ohjelmoituihin
kokonaisuuksiin, joita voi käyttää helposti hyödykseen ja säästyä
suurelta määrältä koodin kirjoittamista. Tämän kurssin tapauksessa
käytämme paljon `requests`-kirjastoa, joka tekee pyyntöjen
lähettämisestä palvelimelle hyvin yksinkertaista.

#### <a name="request"></a>Pyyntö
Pyynnöllä viitataan yksinkertaisesti clientin lähettämään viestiin
palvelimelle. Tälläisen voi luoda requests-kirjastolla esimerkiksi
funktiolla `requests.get()`.

#### <a name="server"></a>Palvelin / server
Palvelimella (/serverillä) viitataan tietokoneeseen, joka odottaa että
*clientit* lähettävät sille pyyntöjä, ja vastaa niihin pyyntöihin
tietyillä tavoin. Esimerkiksi, kun lähetät Googlen palvelimille
pyynnön osoitteeseen "google.com", palvelin huomaa että sinä (client)
haluat Googlen etusivun, joten se rakentaa nettisivun vaatimat tiedot,
ja lähettää ne sinulle. Seuraavaksi selaimesi lukisi nämä tiedot ja
rakentaisi Googlen etusivun.

#### <a name="client"></a>Client
Kun puhutaan verkkoyhteyksistä, clientillä viitataan johonkin
itsenäiseen koneeseen joka voi olla esimerkiksi Raspberry Pi, sinun
läppärisi tai kännykkäsi. Se on laite joka lähettää pyyntöjä
palvelimille.
