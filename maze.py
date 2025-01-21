import pygame
import random

# Maze settings
TILE_SIZE = 40
MAZE_WIDTH, MAZE_HEIGHT = 20, 15  # Number of tiles

def generate_maze():
    """Generates a simple maze using a random algorithm."""
    maze = [[1 for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]

    stack = [(0, 0)]  # Starting position in the maze
    maze[0][0] = 0  # Mark as a path

    while stack:
        current_x, current_y = stack[-1]
        # Get valid neighbors
        neighbors = []
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy
            if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and maze[ny][nx] == 1:
                neighbors.append((nx, ny))

        if neighbors:
            # Choose a random neighbor
            next_x, next_y = random.choice(neighbors)

            # Remove wall between current and next cell
            wall_x, wall_y = (current_x + next_x) // 2, (current_y + next_y) // 2
            maze[wall_y][wall_x] = 0

            # Move to the next cell
            stack.append((next_x, next_y))
            maze[next_y][next_x] = 0  # Mark as a path
        else:
            stack.pop()  # Backtrack

    return maze

def draw_maze(screen, maze):
    wall_rects = []
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == 1:  # If cell is a wall
                rect = pygame.Rect(col_idx * TILE_SIZE, row_idx * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                wall_rects.append(rect)

    # Draw each wall
    for rect in wall_rects:
        pygame.draw.rect(screen, (0, 0, 0), rect)

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
