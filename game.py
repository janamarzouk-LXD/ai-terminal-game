"""Cyber Neon Heist — a terminal-based grid game."""

import random

GRID_SIZE = 5

# Player starts at the top-left corner
player_x = 0
player_y = 0

score = 0
collectible_x = 0
collectible_y = 0
hazard_x = 0
hazard_y = 0


def spawn_collectible() -> None:
    """Place the collectible at a random position not occupied by the player or hazard."""
    global collectible_x, collectible_y
    while True:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if (x, y) != (player_x, player_y) and (x, y) != (hazard_x, hazard_y):
            collectible_x = x
            collectible_y = y
            break


def spawn_hazard() -> None:
    """Place the hazard at a random position not occupied by the player or collectible."""
    global hazard_x, hazard_y
    while True:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if (x, y) != (player_x, player_y) and (x, y) != (collectible_x, collectible_y):
            hazard_x = x
            hazard_y = y
            break


def reset_game() -> None:
    """Reset all game state for a new round."""
    global player_x, player_y, score, collectible_x, collectible_y, hazard_x, hazard_y
    player_x = 0
    player_y = 0
    score = 0
    spawn_collectible()
    spawn_hazard()


PLAYER_EMOJI = "🤖"
COLLECTIBLE_EMOJI = "💾"
HAZARD_EMOJI = "👾"
EMPTY_EMOJI = "·"


def draw_grid(px: int, py: int) -> None:
    """Print the 5x5 grid with themed emojis."""
    for row in range(GRID_SIZE):
        line = ""
        for col in range(GRID_SIZE):
            if col == px and row == py:
                line += PLAYER_EMOJI + " "
            elif col == collectible_x and row == collectible_y:
                line += COLLECTIBLE_EMOJI + " "
            elif col == hazard_x and row == hazard_y:
                line += HAZARD_EMOJI + " "
            else:
                line += EMPTY_EMOJI + " "
        print(line)
    print()  # blank line after the grid


def main() -> None:
    """Outer loop — runs rounds of the game and handles the play-again prompt."""
    global player_x, player_y, score, collectible_x, collectible_y, hazard_x, hazard_y

    WIN_SCORE = 10

    while True:
        reset_game()

        print("\033[2J\033[H", end="")
        print("╔════════════════════════╗")
        print("║   Cyber Neon Heist     ║")
        print("╚════════════════════════╝")
        print()
        print("You are a rogue AI drone infiltrating a high-security")
        print("mega-corp server network. Bypass the firewalls to extract")
        print("encrypted data cores before the system formats your hard drive.")
        print()
        print("WASD to move  |  quit to exit\n")
        print(f"Data Cores: {score}")
        draw_grid(player_x, player_y)

        # --- Inner game loop: runs until win, loss, or quit ---
        result = None  # 'win', 'lose', or 'quit'

        while result is None:
            command = input("> ").strip().lower()

            if command == "quit":
                result = "quit"
                break

            if command == "w" and player_y > 0:
                player_y -= 1
            elif command == "s" and player_y < GRID_SIZE - 1:
                player_y += 1
            elif command == "a" and player_x > 0:
                player_x -= 1
            elif command == "d" and player_x < GRID_SIZE - 1:
                player_x += 1
            elif command:
                print(f"Unknown command: {command}")

            # Check if the player picked up the collectible
            if player_x == collectible_x and player_y == collectible_y:
                score += 1
                if score >= WIN_SCORE:
                    result = "win"
                    break
                spawn_collectible()

            # Check if the player stepped on a hazard
            if player_x == hazard_x and player_y == hazard_y:
                result = "lose"
                break

            # Redraw the grid after every turn
            print("\033[2J\033[H", end="")
            print(f"Data Cores: {score}")
            draw_grid(player_x, player_y)

        # --- Round ended — show result and ask to play again ---
        if result == "quit":
            print("Thanks for playing, mate!")
            break

        if result == "win":
            print("\033[2J\033[H", end="")
            print("System Breached! You successfully extracted")
            print("the data cores and escaped undetected.")
        elif result == "lose":
            print("\033[2J\033[H", end="")
            print("Connection Terminated! The corporate firewall")
            print("detected your presence and wiped your mainframe.")

        while True:
            again = input("Play again? (y/n): ").strip().lower()
            if again == "y":
                print()
                break  # back to outer loop → reset_game()
            elif again == "n":
                print("Thanks for playing, mate!")
                return
            else:
                print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
