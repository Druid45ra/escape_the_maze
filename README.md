# Escape the Maze

Escape the Maze is a simple Python game developed using the Pygame library. The goal of the game is to navigate a player character through a maze while avoiding obstacles and reaching the finish point.

## Features

- Player movement using arrow keys or WASD.
- Randomly generated maze layout.
- Collision detection with walls and obstacles.

## Requirements

- Python 3.10+
- Pygame 2.6.1

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/escape-the-maze.git
   cd escape-the-maze
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the game:
   ```bash
   python main.py
   ```

2. Use the following keys to control the player:
   - Arrow keys or **WASD** for movement.

3. Navigate through the maze and avoid hitting the walls!

## File Structure

```
escape_the_maze/
├── assets/          # Images and other assets
│   ├── player.png
├── main.py          # Main game loop
├── maze.py          # Maze generation logic
├── player.py        # Player class and functionality
├── requirements.txt # Required dependencies
└── README.md        # Project documentation
```

## Customization

- **Maze:** You can adjust the maze size and complexity in `maze.py`.
- **Player:** Modify the player speed, size, or starting position in `player.py`.
- **Obstacles:** Add or remove obstacles as needed by editing the maze layout in `maze.py`.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Pygame Documentation](https://www.pygame.org/docs/)
