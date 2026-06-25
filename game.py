"""A simple text-based terminal game."""

GRID_SIZE = 5

# Player starts at the top-left corner
player_x = 0
player_y = 0


def draw_grid(px: int, py: int) -> None:
    """Print the 5x5 grid, marking the player's position with [P]."""
    for row in range(GRID_SIZE):
        line = ""
        for col in range(GRID_SIZE):
            if col == px and row == py:
                line += "[P]"
            else:
                line += "[ ]"
        print(line)
    print()  # blank line after the grid


def main() -> None:
    """Main game loop — draws the grid, handles WASD movement, and re-renders."""
    global player_x, player_y

    print("Welcome to the Grid Game!")
    print("WASD to move  |  quit to exit\n")

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

        # Redraw the grid after every turn
        print("\033[2J\033[H", end="")
        draw_grid(player_x, player_y)


if __name__ == "__main__":
    main()
