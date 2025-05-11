import pytest
import pygame
import pacman  # імпортуємо весь модуль

# ======= Тести руху Pac-Man'a ==========

@pytest.mark.parametrize("direction, expected_x, expected_y", [
    (0, 102, 100),  # вправо
    (1, 98, 100),   # вліво
    (2, 100, 98),   # вгору
    (3, 100, 102),  # вниз
])
def test_move_player_basic(monkeypatch, direction, expected_x, expected_y):
    monkeypatch.setattr(pacman, "direction", direction)
    monkeypatch.setattr(pacman, "player_speed", 2)
    monkeypatch.setattr(pacman, "turns_allowed", [True, True, True, True])

    start_x, start_y = 100, 100
    new_x, new_y = pacman.move_player(start_x, start_y)
    assert new_x == expected_x
    assert new_y == expected_y

# ======= Тести на зіткнення з привидом ==========

@pytest.fixture
def ghost():
    return pacman.Ghost(
        x_coord=100,
        y_coord=100,
        target=(200, 200),
        speed=2,
        img=None,
        direct=0,
        dead=False,
        box=False,
        id=0
    )


