# Cyber Neon Heist

You are a rogue AI drone infiltrating a high-security mega-corp server network. Bypass the firewalls to extract encrypted data cores before the system formats your hard drive.

Navigate a 5×5 terminal grid, collect data cores, dodge corporate firewalls, and see if you have what it takes to breach the system.

## Features

- **WASD Movement** — Move your drone (`🤖`) around a 5×5 grid with `W` (up), `A` (left), `S` (down), and `D` (right). The grid re-renders after every move, and the player is clamped at the grid boundaries.
- **Collectible Data Cores** — Each `💾` you reach adds one point to your score and respawns at a new random location.
- **Hazard Firewalls** — Hitting a `👾` triggers an instant game over.
- **Win Condition** — Collect 10 data cores to trigger the victory screen.
- **Play Again Prompt** — After a win or loss, you are asked whether you want to play again. Enter `y` to start a fresh round or `n` to exit cleanly.
- **Themed Display** — The game presents a title banner, story intro, and emoji-based grid using `🤖`, `💾`, `👾`, and `·` for empty cells.

## How to Run

Make sure you have Python 3 installed, then launch the game from the terminal:

```bash
python game.py
```

Use the `W`, `A`, `S`, `D` keys to move, type `quit` to exit mid-game, and follow the "Play again?" prompt after each round ends.

### Running Tests

The project includes a suite of automated tests written with pytest. Run them with:

```bash
pytest
```

Or for verbose output:

```bash
pytest -v
```

The test suite covers grid rendering, player boundary clamping, collectible and hazard spawn logic, and state reset — 13 tests in total.

## What I Learned

This project was built iteratively, starting from a bare-bones grid renderer and growing feature by feature. Each stage taught something valuable:

- **Iterative development** — Adding one piece at a time (grid → movement → scoring → hazards → play-again → theming) made it easy to isolate bugs and verify each behaviour before moving on. A working game emerged from small, safe steps rather than a single massive push.
- **Engineering prompts to prevent regression** — Every new feature was expressed as a clear requirement before any code was written. By stating exactly what should happen (and what should *not* happen), it was far easier to spot when a change accidentally broke something that used to work. This is essentially writing a lightweight spec before coding.
- **Using automated tests** — The pytest suite caught regressions immediately. When the grid was re-themed from `[P]` / `[C]` / `[X]` to emojis, two tests failed and pointed right at the impacted assertions. Without tests, that would have been a silent visual bug. Tests also gave confidence when refactoring the game loop to support play-again — a change that touched control flow across the entire `main()` function.
