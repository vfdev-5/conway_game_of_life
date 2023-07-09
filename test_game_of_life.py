from game_of_life import GameOfLife
from game_of_life import create_block


def test__compute_bounds():
    g = GameOfLife(init_state={(0, 0), (10, 2), (5, 6)})
    assert g._bounds == [(0, 0), (10, 6)]


def test_next_block():
    init_state = {(0, 0), (1, 0), (0, 1), (1, 1)}
    g = GameOfLife(init_state=init_state)
    assert g.live_cells == init_state
    g.next()
    assert g.live_cells == init_state
    g.next()
    assert g.live_cells == init_state


def test_next_blinker():
    init_state = {(0, 1), (1, 1), (2, 1)}
    g = GameOfLife(init_state=init_state)
    assert g.live_cells == init_state
    g.next()
    assert g.live_cells == {(1, 0), (1, 1), (1, 2)}
    g.next()
    assert g.live_cells == init_state
    g.next()
    assert g.live_cells == {(1, 0), (1, 1), (1, 2)}


def test_next_toad():
    init_state = {
        (2, 2),
        (3, 2),
        (4, 2),
        (1, 3),
        (2, 3),
        (3, 3),
    }
    next_state = {
        (3, 1),
        (4, 2),
        (4, 3),
        (1, 2),
        (1, 3),
        (2, 4),
    }
    g = GameOfLife(init_state=init_state)
    assert g.live_cells == init_state
    g.next()
    assert g.live_cells == next_state
    g.next()
    assert g.live_cells == init_state
    g.next()
    assert g.live_cells == next_state


def test_create_block():
    b = create_block(10, 10, 5)
    assert len(b) == 25
