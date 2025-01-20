import pygame
import random

# Maze settings
TILE_SIZE = 40
MAZE_WIDTH, MAZE_HEIGHT = 20, 15  # Number of tiles

def generate_maze():
    """Generates a simple maze using a random algorithm."""
    maze = [[1 for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]

    stack = []
    visited = set()

    start_x, start_y = 0, 0  # Starting position in the maze
    stack.append((start_x, start_y))
    visited.add((start_x, start_y))

    while stack:
        current_x, current_y = stack[-1]
        maze[current_y][current_x] = 0  # Mark as a path

        # Get valid neighbors
        neighbors = []
        directions = [
            (0, -2),  # Up
            (0, 2),   # Down
            (-2, 0),  # Left
            (2, 0)    # Right
        ]

        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy
            if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and (nx, ny) not in visited:
                neighbors.append((nx, ny))

        if neighbors:
            # Choose a random neighbor
            next_x, next_y = random.choice(neighbors)

            # Remove wall between current and next cell
            wall_x, wall_y = (current_x + next_x) // 2, (current_y + next_y) // 2
            maze[wall_y][wall_x] = 0

            # Move to the next cell
            stack.append((next_x, next_y))
            visited.add((next_x, next_y))
        else:
            stack.pop()  # Backtrack

    return maze

def draw_maze(screen, maze):
    """Draws the maze on the screen."""
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            if tile == 1:  # Wall
                pygame.draw.rect(
                    screen, (0, 0, 0),
                    (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                )

if __name__ == "__main__":
    pygame.init()

    # Screen settings
    screen_width = TILE_SIZE * MAZE_WIDTH
    screen_height = TILE_SIZE * MAZE_HEIGHT
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze Generator")

    # Generate and draw the maze
    maze = generate_maze()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Clear screen with white
        draw_maze(screen, maze)  # Draw the maze

        pygame.display.flip()

    pygame.quit()
