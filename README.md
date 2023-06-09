# Tetris-game

Pelisovellus noudattaa alkuperäisen Tetris-pelin ominaisuuksia, eli yksinpeli jossa tehtävänä on täyttää pelikentän rivit erimuotoisilla tetrominoilla, jolloin täytetyt rivit katoavat ja pelaaja saa pisteitä. Peli päättyy, kun täyttämättömät rivit saavuttavat pelikentän huipun. Käyttäjien parhaat tulokset tallenntuvat muistiin, jotka näkyvät pelaajille tulostaulussa.

## Releaset
- [Release 1](https://github.com/maxxof/ot-harjoitustyo/releases/tag/viikko5)
- [Release 2](https://github.com/maxxof/ot-harjoitustyo/releases/tag/viikko6)
- [Loppupalautus](https://github.com/maxxof/ot-harjoitustyo/releases/tag/viikko7)
## Dokumentaatio

- [Käyttöohje](https://github.com/maxxof/ot-harjoitustyo/blob/master/tetris-game/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/maxxof/ot-harjoitustyo/blob/master/tetris-game/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/maxxof/ot-harjoitustyo/blob/master/tetris-game/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/maxxof/ot-harjoitustyo/blob/master/tetris-game/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/maxxof/ot-harjoitustyo/blob/master/tetris-game/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/maxxof/ot-harjoitustyo/blob/master/tetris-game/dokumentaatio/testaus.md)

## Käyttöönottaminen

1. Siirrytään projektihakemistoon:

```bash
cd tetris-game
```

2. Asennetaan riippuvuudet:

```bash
poetry install
```


3. Käynnistetään peli:

```bash
poetry run invoke start
```
## Komentorivitoiminnot


### Testaus

Testaus tapahtuu komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti saadaan komennolla:

```bash
poetry run invoke coverage-report
```

Jota pääsee tarkastelemaan komennolla:

```bash
open htmlcov/index.html
```

### Pylint

Koodin laatutarkistus Pylint-työkalulla tapahtuu komennolla:

```bash
poetry run invoke lint
```
