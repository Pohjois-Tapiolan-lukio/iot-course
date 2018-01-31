# Ensimmäinen taulukko, ensimmäiset datat
Tässä tehtävässä luomme palvelimen [API](#api):lla taulukon, ja
laitamme sinne vähän dataa.

### Request-funktio
Jos lähtisimme nyt kirjoittelemaan lisää requests.get-kutsuja,
saisimme kyllä ohjelman valmiiksi, mutta joutuisimme toistamaan
iot.olarinlukio.fi hyvin paljon, ja itsensä toistaminen on
ohjelmoinnissa huono asia. Muutetaan siis kaksi viimeistä riviä
edellisestä tehtävästä omaksi funktiokseen:

```python
def request(call):
    response = requests.get("http://iot.olarinlukio.fi:5000/" + call)
    return response.text
```

Jos vielä haluaisimme kutsua `/heippa`-kutsua, voisimme vain kirjoittaa

```python
request("heippa")
```

### Taulukon luonti
IoT palvelimen API:lla voi luoda uuden taulukon seuraavanlaisella
kutsulla: `api/v1/<nimi>/create/<sarakkeet>` Missä `<nimi>` on
taulukon nimi ja `<sarakkeet>` ovat sarakkeiden nimiä puolipilkuilla
erotettuna, eli jos haluaisit alla olevan taulukon, kirjottaisit
sarakkeisiksi `aika;lampotila`. Eli esimerkiksi:
`api/v1/opiskelija123n_taulukko/create/aika;lampotila`

Taulukkooon voi lisätä uuden rivin dataa kutsulla
`api/v1/<nimi>/insert/<arvot>` missä `<nimi>` on jälleen taulukon
nimi, ja `<arvot>` ovat lisättävät arvot samalla lailla muotoillusti
kuin luodessa taulukkoa. Esimerkiksi tämän taulukon toisen rivin voisi
lisätä seuraavalla kutsulla:
`api/v1/opiskelija123n_taulukko/insert/1;23`

| aika | lampotila |
|------|-----------|
| 0    | 23        |
| 1    | 23        |
| 2    | 24        |

Tehdään nyt hyvin yksinkertainen ohjelma, joka luo joka toinen sekunti
uuden datapisteen, nostaen arvoa yhdellä joka kerta.

Aluksi importataan `sleep`-funktio, jotta voimme ajoittaa
toistolausekkeen. Lisää siis koodin alkuun:

```python
from time import sleep
```

Luodaan sitten toistolauseke, jossa meillä on lähetettävä arvo
valmiina:

```python
arvo = 0
while True:
    arvo += 1
    print(arvo)
    sleep(2)
```

Nyt siirrytään tiedonsiirto-osaan. Lisää aiemman osion alkuun kutsu
jolla luodaan uusi taulukko (muista vaihtaa koodissa `<taulukko_nimi>`
joksikin omaksi nimeksi):

```python
request("api/v1/<taulukko_nimi>/create/nouseva_numero")
arvo = 0
...
```

Ja viimeisenä lisätään datan lähetys palvelimelle (printin jälkeen,
toistolausekkeen sisällä):

```python
    ...
    print(arvo)
    request("api/v1/<taulukko_nimi>/insert/" + str(arvo))
    sleep(2)
    ...
```

Nyt voit selaimellasi mennä osoitteeseen
`http://iot.olarinlukio.fi/api/v1/<taulukko_nimi>/print` ja näet
lähetetyn datan. Muista jälleen muuttaa linkissä `<taulukko_nimi>`
oman taulukkosi nimeksi.


---
### Hieman termistöä
#### <a name="api"></a>API
API, eli Application Programming Interface on termi jota käytetään,
kun puhutaan jonkinlaisesta rajapinnasta minkä kautta voi käyttää
ohjelmistoa, kirjastoa, tai kuten tässä tapauksessa, palvelinta. API
koostuu yleensä jonkinlaisista kutsuista, palvelimien tapauksessa
usein tietyllä tavoin kirjoitetuista URL-osoitteista.
