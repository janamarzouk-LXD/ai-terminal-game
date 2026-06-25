"""A simple text-based terminal game."""

import random

GRID_SIZE = 5

# Player starts at the top-left corner
player_x = 0
player_y = 0

score = 0
collectible_x = 0
collectible_y = 0


def spawn_collectible() -> None:
    """Place the collectible at a random position not occupied by the player."""
    global collectible_x, collectible_y
    while True:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if (x, y) != (player_x, player_y):
            collectible_x = x
            collectible_y = y
            break


def draw_grid(px: int, py: int) -> None:
    """Print the 5x5 grid, marking the player [P] and collectible [C]."""
    for row in range(GRID_SIZE):
        line = ""
        for col in range(GRID_SIZE):
            if col == px and row == py:
                line += "[P]"
            elif col == collectible_x and row == collectible_y:
                line += "[C]"
            else:
                line += "[ ]"
        print(line)
    print()  # blank line after the grid


def main() -> None:
    """Main game loop — movement, collectible pickup, and win condition."""
    global player_x, player_y, score, collectible_x, collectible_y

    WIN_SCORE = 10

    spawn_collectible()

    print("\033[2J\033[H", end="")
    print("Welcome to the Grid Game!")
    print("WASD to move  |  quit to exit\n")
    print(f"Score: {score}")
    draw_grid(player_x, player_y)

    while True:
        command = input("> ").strip().lower()

        if command == "quit":
            print("Thanks for playing, mate!")
            break

        moved = False

        if command == "w" and player_y > 0:
            player_y -= 1
            moved = True
        elif command == "s" and player_y < GRID_SIZE - 1:
            player_y += 1
            moved = True
        elif command == "a" and player_x > 0:
            player_x -= 1
            moved = True
        elif command == "d" and player_x < GRID_SIZE - 1:
            player_x += 1
            moved = True
        elif command:
            print(f"Unknown command: {command}")

        # Check if the player picked up the collectible
        if player_x == collectible_x and player_y == collectible_y:
            score += 1
            if score >= WIN_SCORE:
                print("\033[2J\033[H", end="")
                print("Congratulations! You collected all 10 items!")
                print("Thanks for playing, mate!")
                break
            spawn_collectible()

        # Redraw the grid after every turn
        print("\033[2J\033[H", end="")
        print(f"Score: {score}")
        draw_grid(player_x, player_y)


if __name__ == "__main__":
    main()
