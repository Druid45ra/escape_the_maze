import pygame
import os

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape the Maze")

# Colors
duck_egg_green = (124, 252, 0)
obstacle_color = (0, 0, 0)  # Obstacles color (black)

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

# Initial player position
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5  # Player speed

# Obstacles (coordinates and dimensions)
obstacles = [
    pygame.Rect(100, 150, 200, 20),  # Obstacle 1 (moved down)
    pygame.Rect(500, 100, 20, 200),  # Obstacle 2 (moved right)
    pygame.Rect(200, 400, 200, 20),  # Obstacle 3 (moved down)
    pygame.Rect(600, 450, 20, 100),  # Obstacle 4 (moved right)
]

# Function to check collision with obstacles
def check_collision(x, y, obstacles):
    player_rect = pygame.Rect(x, y, player_width, player_height)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True  # Collision
    return False  # No collision

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of pressed keys
    keys = pygame.key.get_pressed()
    
    # Player movement
    new_x, new_y = player_x, player_y
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        new_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        new_x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        new_y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        new_y += player_speed

    # Check collision with obstacles before changing position
    if not check_collision(new_x, new_y, obstacles):
        player_x, player_y = new_x, new_y

    # Fill the background color
    screen.fill(duck_egg_green)

    # Draw obstacles on the screen
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, obstacle)

    # Display the player
    screen.blit(player_img, (player_x, player_y))

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

pygame.quit()
