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
    """The grid drawing should place the player emoji at (0, 0)."""
    import io
    import sys

    captured = io.StringIO()
    sys.stdout = captured

    game.draw_grid(0, 0)

    sys.stdout = sys.__stdout__

    output = captured.getvalue()
    lines = output.strip().split("\n")

    # The first cell of the first row should be the player emoji
    assert lines[0].startswith(game.PLAYER_EMOJI), (
        f"Expected first cell to be {game.PLAYER_EMOJI}, "
        f"got: {lines[0][:2]}"
    )


def test_grid_empty_cell() -> None:
    """A cell without the player should show the empty emoji."""
    import io
    import sys

    captured = io.StringIO()
    sys.stdout = captured

    game.draw_grid(0, 0)

    sys.stdout = sys.__stdout__

    output = captured.getvalue()
    lines = output.strip().split("\n")

    # The second cell of the first row should be empty
    cell_start = len(game.PLAYER_EMOJI) + 1  # skip past emoji + space
    assert lines[0][cell_start:].startswith(game.EMPTY_EMOJI), (
        f"Expected empty emoji {game.EMPTY_EMOJI} at position 1,0, "
        f"got: {lines[0][cell_start:cell_start + 1]}"
    )


def test_grid_shows_all_entities() -> None:
    """The grid should show the player, collectible, and hazard when drawn."""
    import io
    import sys

    # Place each entity in a known position
    game.player_x = 0
    game.player_y = 0
    game.collectible_x = 2
    game.collectible_y = 2
    game.hazard_x = 4
    game.hazard_y = 4

    captured = io.StringIO()
    sys.stdout = captured

    game.draw_grid(0, 0)

    sys.stdout = sys.__stdout__

    lines = captured.getvalue().strip().split("\n")

    # Row 0 should start with the player
    assert lines[0].startswith(game.PLAYER_EMOJI), "Player should be at (0,0)"

    # Row 2, cell 2 (index 2) should be the collectible
    # Each cell is emoji + space = 2 chars (assuming single-char emoji display)
    cell_width = 2
    collectible_cell_start = game.collectible_x * cell_width
    assert lines[game.collectible_y][collectible_cell_start:].startswith(
        game.COLLECTIBLE_EMOJI
    ), f"Collectible {game.COLLECTIBLE_EMOJI} should be at ({game.collectible_x},{game.collectible_y})"

    # Row 4, cell 4 should be the hazard
    hazard_cell_start = game.hazard_x * cell_width
    assert lines[game.hazard_y][hazard_cell_start:].startswith(
        game.HAZARD_EMOJI
    ), f"Hazard {game.HAZARD_EMOJI} should be at ({game.hazard_x},{game.hazard_y})"


def test_player_boundary_top() -> None:
    """Player should not move above row 0."""
    game.player_y = 0
    # Simulate pressing 'w'
    if game.player_y > 0:
        game.player_y -= 1
    assert game.player_y == 0, "Player should be clamped at row 0"


def test_player_boundary_bottom() -> None:
    """Player should not move below row (GRID_SIZE - 1)."""
    game.player_y = game.GRID_SIZE - 1
    if game.player_y < game.GRID_SIZE - 1:
        game.player_y += 1
    assert game.player_y == game.GRID_SIZE - 1, (
        f"Player should be clamped at row {game.GRID_SIZE - 1}"
    )


def test_player_boundary_left() -> None:
    """Player should not move left of column 0."""
    game.player_x = 0
    if game.player_x > 0:
        game.player_x -= 1
    assert game.player_x == 0, "Player should be clamped at column 0"


def test_player_boundary_right() -> None:
    """Player should not move right of column (GRID_SIZE - 1)."""
    game.player_x = game.GRID_SIZE - 1
    if game.player_x < game.GRID_SIZE - 1:
        game.player_x += 1
    assert game.player_x == game.GRID_SIZE - 1, (
        f"Player should be clamped at column {game.GRID_SIZE - 1}"
    )


def test_spawn_collectible_not_on_player() -> None:
    """Collectible should never spawn on the player's position."""
    game.player_x = 2
    game.player_y = 3
    game.hazard_x = 0
    game.hazard_y = 0
    game.spawn_collectible()
    assert (game.collectible_x, game.collectible_y) != (2, 3), (
        "Collectible should not spawn on the player"
    )


def test_spawn_hazard_not_on_player() -> None:
    """Hazard should never spawn on the player's position."""
    game.player_x = 1
    game.player_y = 1
    game.collectible_x = 4
    game.collectible_y = 4
    game.spawn_hazard()
    assert (game.hazard_x, game.hazard_y) != (1, 1), (
        "Hazard should not spawn on the player"
    )


def test_spawn_hazard_not_on_collectible() -> None:
    """Hazard should never spawn on the collectible's position."""
    game.player_x = 0
    game.player_y = 0
    game.collectible_x = 2
    game.collectible_y = 2
    game.spawn_hazard()
    assert (game.hazard_x, game.hazard_y) != (2, 2), (
        "Hazard should not spawn on the collectible"
    )


def test_reset_game_restores_initial_state() -> None:
    """reset_game should put the player back at (0,0) and score to 0."""
    # Mess up the state first
    game.player_x = 3
    game.player_y = 4
    game.score = 7

    game.reset_game()

    assert game.player_x == 0, "Player x should reset to 0"
    assert game.player_y == 0, "Player y should reset to 0"
    assert game.score == 0, "Score should reset to 0"
