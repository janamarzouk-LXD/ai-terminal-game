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
    """Main game loop that draws the grid and waits for input."""
    print("Welcome to the Grid Game!")
    print("Type 'quit' to exit.\n")

    draw_grid(player_x, player_y)

    while True:
        command = input("> ").strip().lower()

        if command == "quit":
            print("Thanks for playing, mate!")
            break
        elif command:
            print(f"Unknown command: {command}")
            print()


if __name__ == "__main__":
    main()
