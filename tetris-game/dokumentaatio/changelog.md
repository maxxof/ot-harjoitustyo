## Viikko 3

- Alustettu projekti
- Luotu sovelluksen toiminnan kannalta välttämättömät luokat: MainMenu, Button, Username ja GameLoop
- MainMenu-luokka huolehtii päävalikkonäkymän toiminnasta
- Button-luokka on vastuussa painikkeiden toiminnasta
- Username-luokka huolehtii käyttäjätunnuksen syötöstä
- GameLoop-luokka vastaa pelisilmukkaa, jossa Tetris-peliä tullaan pelaamaan
- Lisätty minimaalinen visuaalinen näkymä, start ja exit painikkeet
- Testattu, että pelisilmukka toimii

## Viikko 4

- Luotu GameEngine-luokka, joka on vastuussa tetris-pelin logiikasta
- Luotu Tetromino-luokka, joka edustaa jokaista tetromino-objektia
- Lisätty pelin toiminnan kannalta välttämätöntä logiikkaa pelimoottoriin
- Koodin refaktorointia (GameLoop, GameEngine)
- Pelin ensimmäinen toimiva versio, jossa suurin osa toiminnallisuuksia
  - Tetrominot renderöityvät ja putoavat alas
  - Tetrominoja voi liikuttaa
  - Tetrominot kasaantuvat ruudukon pohjalle
  - Pelisessio loppuu kun tetrominot kasaantuu katon yli
  - Siirtyminen takaisin päävalikkoon
- Otettu pylint käyttöön, korjattu suurimman osan pylint-virheistä
- Lisätty yksikkötesteja
  - Testattu Tetromino-luokkaa käyttäen GameEngine-luokkaa
  - Testattu Username-luokkaa
  - Testikattavuus 35%
- Lisätty arkkitehtuurikuvaus dokumentaatioon
  - Luotu sovelluksen luokkakaavio

## Viikko 5
- Lisätty uusi toiminnallisuus: pelirivien tyhjennys
  - Kun pelirivi täytetään blokeilla, tyhjennetään rivi ja pudotetaan ylhäällä olevat blokit alas
- Lisätty pisteytyslogiikka
 - Jokaisesta tyhjennetystä rivistä + 100 pistettä
- Lisätty yksikkötesti
  - Testattu GameEngine-luokkaa
  - Testikattavuus 41%
- Koodin pientä refaktorointa GameEngine-moduulissa
- Pylint-virheiden korjaamista
- Päivitetty arkkitehtuurikuvaus
  - Luotu sekvenssikaavio sovelluksen avaamisesta ja pelisilmukan käynnistämisestä
- Luotu ensimmäinen GitHub Release: Release 1
 
## Viikko 6
- Lisätty uusi toiminnallisuus: vuorossa seuraavan olevan tetrominon piirtäminen
- Lisätty viesti pelin häviämisen yhteydessä
  - Viesti ilmoittaa saaduista pisteistä, jotka tullaan tallentamaan pysyvästi seuraavissa päivityksissä
- Luotu docstring-dokumentaatio jokaiselle projektin luokalle ja suurimmalle osalle metodeista
- Luotu pelin käyttöohje
- Luotu toinen GitHub Release: Release 2

## Viikko 7
- Lisätty uusi toiminnallisuus: pisteiden tallennus- ja lukulogiikka
  - Luotu luokka, joka on vastuussa pelipisteiden hallinnasta
- Koodin refaktorointia
- Sovelluksen arkkitehtuurikuvauksen parantaminen
- Vaatimusmäärittelyn päivitys
- Loppupalautus
  Luotu viimeinen GitHub Release: loppupalautus