"""Tests for the grid game."""

import game


def test_grid_size() -> None:
    """The grid should be 5x5."""
    assert game.GRID_SIZE == 5


def test_player_starts_at_origin() -> None:
    """The player should begin at position (0, 0)."""
    assert game.player_x == 0
    assert game.player_y == 0


def test_grid_contains_player() -> None:
    """The grid drawing should place a [P] at the player's position."""
    # We can capture what draw_grid prints to check it looks right
    import io
    import sys

    # Redirect stdout into a string buffer
    captured = io.StringIO()
    sys.stdout = captured

    game.draw_grid(0, 0)

    # Restore stdout
    sys.stdout = sys.__stdout__

    output = captured.getvalue()

    # The first cell of the first row should contain [P]
    lines = output.strip().split("\n")
    assert lines[0].startswith("[P]"), (
        f"Expected first cell to be [P], got: {lines[0][:3]}"
    )


def test_grid_empty_cell() -> None:
    """A cell without the player should be [ ]."""
    import io
    import sys

    captured = io.StringIO()
    sys.stdout = captured

    game.draw_grid(0, 0)

    sys.stdout = sys.__stdout__

    output = captured.getvalue()
    lines = output.strip().split("\n")

    # Second cell of the first row should be empty
    assert lines[0][3:6] == "[ ]", (
        f"Expected [ ] at position 1,0, got: {lines[0][3:6]}"
    )
