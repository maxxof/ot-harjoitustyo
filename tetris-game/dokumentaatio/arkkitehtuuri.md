# Sovelluksen arkkitehtuurikuvaus
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
  
  MainMenu "1" -- "1" GameLoop
  GameLoop "1" -- "1" GameEngine
  GameEngine "1" -- "2" Tetromino
  MainMenu "1" -- "1" Username
  MainMenu "1" -- "2" Button
  GameLoop "1" -- "1" Button
  EventQueue "1" -- "1" MainMenu
  EventQueue "1" -- "1" GameLoop
  Username "1" -- "1" GameLoop
  
  
