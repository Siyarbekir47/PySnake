# PySnake 🐍

PySnake is a simple snake game implemented in Python using the Turtle graphics library. The player controls a snake using the arrow keys, and the goal is to eat food to grow the snake while avoiding collisions with walls and the snake's own tail.

## Features

- Control the snake using arrow keys (`Up`, `Down`, `Left`, `Right`).
- The snake grows each time it eats food.
- The score increases as the snake eats food.
- The game ends if the snake collides with the walls or its own body.
- A scoreboard keeps track of the score during the game.

## Getting Started

### Prerequisites

- Python 3.x
- Turtle module (usually comes with Python, but can be installed via `pip` if necessary)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/pysnake.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pysnake
    ```

3. Ensure you have the required modules:

    ```bash
    pip install PythonTurtle
    ```

### Running the Game

1. Run the main Python file:

    ```bash
    python main.py
    ```

2. Control the snake using the arrow keys (`Up`, `Down`, `Left`, `Right`).

### Game Rules

- **Eat food**: The snake will grow, and your score will increase.
- **Avoid walls**: If the snake collides with a wall, the game is over.
- **Avoid the tail**: If the snake runs into its own body, the game is over.

## Project Structure

- `main.py`: The main game logic.
- `Class/snake.py`: The `Snake` class, which handles the snake's movement and growth.
- `Class/food.py`: The `Food` class, which randomly generates food positions.
- `Class/scoreboard.py`: The `Scoreboard` class, which handles the score display and game over messages.

## Controls

- `Up Arrow` - Move the snake up
- `Down Arrow` - Move the snake down
- `Left Arrow` - Move the snake left
- `Right Arrow` - Move the snake right

## Screenshots


## Contributing

Feel free to submit issues or pull requests if you would like to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy playing PySnake! 🎮
