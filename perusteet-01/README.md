# Projektin luominen
Tämä tehtävä toimii perustana kaikille muille tehtäville tämän kurssin aikana.
Tässä opetetaan kuinka luodaan Git-repository, jolla tulet julkaisemaan
tekemäsi koodit. Kirjoitetaan myös lyhyt ohjelma, Gitin toimintojen
demonstroimiseksi.

### Gitin asennus
Linuxilla on yleensä Git valmiiksi asennettuna. Linkit asennusohjelmiin:
- [Windows](https://git-scm.com/download/win)
- [Mac](https://git-scm.com/download/mac)
- [Linux](https://git-scm.com/download/linux)

### Projektikansion luominen
1. Luo projektillesi hakemisto. Ensimmäisenä luo `iot-kurssi` niminen hakemisto
Documents- tai Tiedostot-hakemistoon. Tulet laittamaan kaikki kurssin tehtävät
tämän hakemiston alihakemistoihin.
2. Avaa komentorivi hakemistoon `iot-kurssi`. Ohjeita komentorivin käyttöön
löytyy [täältä](../KOMENTORIVI.md), mutta tässä on ohjeet jokaiselle alustalle:
- Windows: avaa `iot-kurssi`-hakemisto Resurssienhallinnassa, oikea-klikkaa,
ja valitse "Git Bash Here".
- Mac ja Linux: avaa haun avulla Pääte tai Terminal. Siirry päätteessä
Documents-hakemistoon komennolla `cd Documents`, ja sitten kansioon
`iot-kurssi` komennolla `cd iot-kurssi`.

Komentorivillä jatketaan kohdassa **Git-repositoryn lataaminen koneelle**.

### Git-repositoryn luominen
1. Luo uudet GitHub tunnukset. Mikäli sinulla on jo GitHub-tunnukset, on
suositeltavaa tehdä "koulutunnukset", jottei henkilökohtaiset projektisi
sekoitu koulutöihin.
2. Aktivoi tilisi sähköpostista ja kirjaudu sisään.
3. Klikkaa GitHubin etusivun oikeassa yläkulmassa olevaa `+`-merkkiä, ja
valitse `New repository`.
4. Kirjoita nimeksi `perusteet-01`, Descriptioniin voit laittaa mitä vain
(tai ei mitään), ja lopuksi klikkaa vielä valintalaatikosta
"Initialize this repository with a README". *Tämä luo sinulle valmiiksi ns.
README-tiedoston projektillesi. README-tiedostoihin kirjoitetaan yleensä
ohjeet ohjelman käyttöön, ja tietoa siitä mitä ohjelma tekee.*
5. Luo repository napilla `Create repository`, ja kopioi avautuneen sivun
osoite. (Osoite on tyyliä `https://github.com/oppilas123/perusteet-01`)

### Git-repositoryn lataaminen koneelle
1. Palaa takaisin komentoriville jonka avasit aikaisemmin, kansiossa
`iot-kurssi`.
2. Kutsu komento `git clone <url>` missä korvaat `<url>` edellisessä
kohdassa kopioimallasi osoittella.
3. Siirry projektikansioon komennolla `cd perusteet-01`.

### Koodin lisääminen
1. Tämän tehtävän tarkoitus on keskittyä Gitin opiskeluun, joten tehdään
hyvin yksinkertainen ohjelma. Avaa kooditiedosto komennolla `idle main.py`
2. Kirjoita tiedostoon
```python
print("Hello, world!")
```
3. Tallenna tiedosto, ja sulje IDLE.

### Gitille tunnistautuminen
1. Jotta voimme lisätä koodia, meidän pitää määritellä kuka olemme, jotta Git
tietää kenen nimissä tehdä asioita.
2. Asettaaksesi nimesi, käytä komentoa
`git config --global user.name "Opiskelija Opiskelevainen"`
3. Asettaaksesi sähköpostisi (käytä samaa kuin GitHubissa), käytä komentoa
`git config --global user.email "opiskelija.opiskelevainen@eduespoo.fi"`

### Git-repositoryn päivittäminen
1. Nyt kun olemme lisänneet koodia, voimme tarkistaa mitä muutoksia Git
näkee projektissamme komennolla `git status`. Tämä komento kertoo tämänhetkiset
muutokset repositoryssämme.
2. Lisätäksemme muutokset Gittiin, kutsutaan aluksi komentoa `git add -A`.
Mikäli nyt kutsut komennon `git status`, huomaat että muutokset ovat eivät
ole enää "untracked", vaan "commitattavia muutoksia".
3. Luodaan uusi versio projektistamme komennolla `git commit -m "Add code"`.
Gitissä projektit koostuvat "commiteista", jotka ovat käytännössä vain
koodi-lisäyksiä joita kuka tahansa voi tehdä. `-m "Add code"` kohdassa lisätään
ns. "commit message" jonka on tarkoitus kuvailla mitä muutettiin.
4. Nyt mikäli kutsut `git status`, huomaat ettei muutoksia ole listattu. Tämä
johtuu siitä, että nyt lisäämäsi muutokset ovat osa repositoryn versiohistoriaa,
eli ne ovat tavallaan nyt "osa projektia".
5. Viimeisenä lähetetään muutokset GitHubiin, komennolla `git push`.
Nyt tekemäsi muutokset löytyvät GitHubista kun menet selaimella katsomaan, ja
muut ihmiset, kuten kurssitoverisi, voivat ladata uuden version projektistasi.
