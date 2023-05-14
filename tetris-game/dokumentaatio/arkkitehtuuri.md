# Sovelluksen arkkitehtuurikuvaus

## Käyttöliittymä

Käyttöliittymä koostuu kahdesta eri osasta: päävalikko-silmukasta ja pelisilmukasta. Molemmilla on omat luokkaansa, jotka ovat vastuussa näiden silmukoiden eri toiminnallisuuksista: `MainMenu` ja `GameLoop`
Siirto silmukasta toiseen tapahtuu seuraavilla tavoilla:
1. Päävalikko -> pelisilmukka: poistutaan `MainMenu`:n while-silmukasta ja kutsutaan metodia, joka luo uuden pelisilmukan `GameLoop`ja käynnistää sen.
2. Pelisilmukka -> päävalikko: poistutaan `GameLoop`:in while-silmukasta ja palautetaan pelisilmukkaa kutsuvalle metodille käyttäjätunnus ja saadut pisteet. Nyt kutsuva metodi käynnistää päävalikon uudestaan tietojen päivittämisen jälkeen.


## Sovelluslogiikka
Ohjelman luokkakaavio ja luokkien oleellisimmat metodit
```mermaid
classDiagram
  class MainMenu{
    start_main_menu()
    start_game_loop()
  }
  class GameLoop{
    start()
  }
  class EventQueue{
    get()
  }
  class Button{
    draw()
  }
  class Username{
    render()
    add_char()
    backspace()
  }
  class Tetromino{
    move_left()
    move_right()
    move_down()
    move_up()
    rotate()
  }
  class GameEngine{
    create_grid()
    render_grid()
    tetromino_fall()
    lock_and_switch_tetromino()
    check_if_lost()
  }
  class StorageController{
    get_scores()
    save_scores()
  }
  
  MainMenu "1" -- "1" GameLoop
  GameLoop "1" -- "1" GameEngine
  GameEngine "1" -- "2" Tetromino
  MainMenu "1" -- "1" Username
  MainMenu "1" -- "2" Button
  GameLoop "1" -- "1" Button
  EventQueue "1" -- "1" MainMenu
  EventQueue "1" -- "1" GameLoop
  Username "1" -- "1" GameLoop
  MainMenu "1" -- "1" StorageController
  ```
  
  ## Päätoiminnallisuudet
  ### Sovelluksen avaaminen ja pelisilmukan käynnistäminen
  
  Sovelluksen käynnistäessä eteneminen pelisilmukkaan on havainnollistettu seuraavassa sekvenssikaaviossa:
  
  ```mermaid
  sequenceDiagram
  actor User
  User ->> main: open program
  main ->> MainMenu: MainMenu()
  main ->> MainMenu: start_main_menu()
  
  MainMenu ->> Username: Username()
  MainMenu ->> Button: Button() x 2
  
  User ->> MainMenu: enter name
  User ->> MainMenu: click "start" button
  
  MainMenu ->> MainMenu: start_game_loop()
  MainMenu ->> GameLoop: GameLoop()
  MainMenu ->> GameLoop: start()
  ```
  
  Kun indeksitiedosto suoritetaan, luodaan MainMenu-olio, joka vastaam käyttäjätunnuksen syötöstä, tulostaulukosta ja pelisilmukan käynnistämisestä.
  
  ### Pelisilmukka ja pelin suorittaminen
  
  Siirryttyään päävalikko-silmukasta pelisilmukkaan luodaan pelilogiikasta vastaava GameEngine-olio ja käynnistetään itse silmukka, jossa kuunnellaan käyttäjän syöttöä ja päivitetään peliruudukkoa sen mukaan.
  
  ```mermaid
  sequenceDiagram
  actor User
  GameLoop ->> GameLoop: GameEngine()
  GameLoop ->> GameEngine: create_grid()
  User ->> GameLoop: click arrow key ">"
  GameLoop ->> GameEngine: move_tetromino_right()
  GameEngine ->> Tetromino: move_right()
  GameLoop ->> GameEngine: update_grid()
  GameLoop ->> GameEngine: render_grid()
  ```
  
  Esimerkiksi oikean nuolinäppäimen painatessa silmukka kutsuu oman GameEngine-olion metodia `move_tetromino_right`, joka jälkeenpäin kutsuu nykyisen Tetromino-olion omaa metodia `move_right()`, joka muuttaa x-akseli attribuuttiaan.
  
## Tietojen paikallinen pysyväistallennus

Juurihakemiston luokka `StorageController` on vastuussa kaikesta pysyväistallennuksesta ja tiedon lukemisesta tiedostosta. Luokka käyttää pakkauksen _storage_ CSV-tiedostoa highscores.csv, johon tallennetaan top-5 parhaat tulokset. `StorageController` myös lukee tiedostoa, järjestää pisteet suuruusjärjestyksessä ja palauttaa listana tupleista (käyttäjätunnus, pisteet) muodossa `MainMenu`-luokalle, josta se renderöi saatu data tulostaulukkoon.

## Ohjelmiston arkkitehtuurin parantamismahdollisuuksia
  
### Käyttöliittymä

Käyttöliittymästä vastuussa oleva koodi on mahdollista refaktoroida siistimmäksi; koodit, jotka renderöivät grafiikkaa ovat samaoissa metodeissa ja luokissa, jotka käsittelevät sovelluslogiikkaa. Esimerkiksi `GameEngine`-luokka sisältää paljon renderöintikoodia, joka on mahdollista eristää omaksi renderöinti-luokaksi.

  
  
  
  
  
  
  
  
