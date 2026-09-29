## Задание 1.1

| № | Что | Где в исходном коде | Куда перенести |
|---|-----|---------------------|----------------|
| 1 | `high_score`, `current_score`, `game_state`, `difficulty_level`, `is_sound_on` | Глобальные переменные | **Game** |
| 2 | `lives`, `hammer_is_swinging` | Глобальные переменные | **Player** |
| 3 | `is_visible`, `speed`, `points` | Словарь `rat` | **Rat** |
| 4 | `holes_count`, `active_rats` | Глобальные переменные | **GameField** |
| 5 | `position_x`, `position_y`, `is_occupied` | Неявно в индексе `hole` | **Hole** |
| 6 | `start_game()`, `pause_game()`, `restart_game()` | Функции | **Game** |
| 7 | `spawn_rat()`, `update_field()` | Функции | **GameField** |
| 8 | `hit_rat()`, `lose_life()`, `add_score()` | Функции | **Player** |
| 9 | `pop_up()`, `hide()`, `get_hit()` | Логика в `spawn_rat()` | **Rat** |
| 10 | `show_menu()`, `show_scoreboard()`, `draw_hammer_animation()` | `print` / `input` | **UI** |

## Задание 1.2

1. **Какие классы выделены?**
`Game`, `Player`, `Rat`, `GameField`, `Hole`, `UI` — каждый отвечает за свою зону ответственности.

2. **Приватные атрибуты:**
Все атрибуты, кроме констант, приватные (`_`), так как требуется валидация и контроль доступа.

3. **Публичные методы:**
`start_game()`, `hit_rat()`, `pop_up()` и т.д. — формируют публичный интерфейс классов.

4. **God Object в исходном коде:**
Да, процедурный код — классический пример **God Object**: все функции работают с глобальными переменными, нет чёткого разделения ответственности.
