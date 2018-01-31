# Komentorivin perusteet
Tässä dokumentissa on hieman perusasioita komentorivin käytöstä ja toiminnoista.

### Perusasioita
- Komentorivi on aina jossain hakemistossa. Yleensä käynnistettäessä se avautuu
käyttäjän kotihakemistoon, mutta usein tulet avaamaan sen tarkoituksellisesti
johonkin tiettyyn hakemistoon. Hakemiston polku on vasemmalla kohdasta johon kirjoitat
komennon.
- Windows: Voit avata komentorivin tiettyyn hakemistoon avaamalla kyseisen hakemiston
Resurssienhallinnassa, oikea-klikkaamalla valkoista aluetta, ja valitsemalla
"Git Bash Here" vaihtoehdon.
- Mac ja Linux: Komentoriviä kutsutaan yleensä termeillä "pääte" ja "terminal"
näillä alustoilla, joten kun etsit komentoriviä koneeltasi, käytä näitä
hakusanoina.
- Joskus saatat nähdä komentojen perässä viivalla alkavia merkintöjä kuten
`-r` tai `-m` tai `--amend`.
Nämä ovat ns. flageja, joilla voidaan ohjata komennon käyttäytymistä.
Yksinkertainen esimerkki on `-r` komennolla `rm`, joka yhden tiedoston
poistamisen sijaan käykin rekursiivisesti kansion läpi ja poistaa kaiken. Joskus
flagit tarvitsevat lisätietoa, kuten esimerkiksi `git commit`:n `-m`-flag.
Sitä käyttäessä `-m`:n jälkeen kirjoitetaan tekstiä heittomerkkien väliin, eli:
`-m "Tekstiä"`.

### Yleisiä komentoja komentoriville
- `ls`: Tuottaa listan tiedostoista ja hakemistoista tämänhetkisessä hakemistossa.
- `cd <hakemisto>`: Siirtyy annettuun hakemistoon. Esimerkiksi, jos `ls` listasi
yhdeksi kansioksi `iot-kurssi`, voit käyttää komentoa `cd iot-kurssi` siirtyäksesi
kyseiseen kansioon. Voit myös kirjoittaa pidempiä polkuja,
esimerkiksi `cd Documents/iot-kurssi/`
- `mkdir <hakemisto>`: Luo uuden hakemiston annetulla nimellä.
- `rm <tiedosto>`: Poistaa annetun tiedoston.
- `rm -r <kansio>`: Poistaa kansion ja kaikki sen sisällöt.
(Nippelitietoa: -r tulee sanasta recursive, ja tämä komento käy hakemiston läpi
"rekursiivisesti", eli se käy myös hakemiston sisäiset hakemistot jne. läpi, ja
poistaa kaikki vastaantulevat tiedostot.)
