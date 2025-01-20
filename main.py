import pygame
import os
from maze import generate_maze, draw_maze
from player import Player

# Maze settings
maze = generate_maze()
TILE_SIZE = 40

# Player settings
player = Player(0, 0, TILE_SIZE, TILE_SIZE, speed=5)

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape the Maze")

# Colors
duck_egg_green = (124, 252, 0)  # Background color
obstacle_color = (0, 0, 0)      # Obstacles color (black)

# Clock and variables
clock = pygame.time.Clock()

# Asset directory
ASSET_DIR = "assets"

# Load player image
player_path = os.path.join(ASSET_DIR, "player.png")
try:
    player_img = pygame.image.load(player_path)
except pygame.error as e:
    print(f"Unable to load image at {player_path}: {e}")
    pygame.quit()
    exit()

# Resize player image
player_width, player_height = 40, 40
player_img = pygame.transform.scale(player_img, (player_width, player_height))

# Initial player position (top-left corner)
player_x, player_y = 0, 0
player_speed = 5  # Player speed

# Obstacles (coordinates and dimensions)
obstacles = [
    pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    for y, row in enumerate(maze)
    for x, tile in enumerate(row)
    if tile == 1
]


# Function to check collision with obstacles
def check_collision(x, y):
    player_rect = pygame.Rect(x, y, player_width, player_height)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True  # Collision detected
    return False  # No collision

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of pressed keys
    keys = pygame.key.get_pressed()

    # Move the player
    player.move(keys, obstacles=[])

    # Draw everything
    screen.fill(duck_egg_green)  # Draw background
    draw_maze(screen, maze)  # Draw maze
    player.draw(screen)  # Draw player

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
    
    # Calculate new position
    new_x, new_y = player_x, player_y
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        new_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        new_x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        new_y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        new_y += player_speed

    # Check collision with obstacles before updating position
    if not check_collision(new_x, new_y):
        player_x, player_y = new_x, new_y

    # Draw everything
    screen.fill(duck_egg_green)  # Draw background

    for obstacle in obstacles:  # Draw obstacles
        pygame.draw.rect(screen, obstacle_color, obstacle)

    screen.blit(player_img, (player_x, player_y))  # Draw player

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

pygame.quit()
