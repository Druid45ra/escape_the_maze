import pygame
import os

# Inițializare Pygame
pygame.init()

# Setări ecran
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape the Maze")

# Culoare verde ou de rață
duck_egg_green = (124, 252, 0)
obstacle_color = (0, 0, 0)  # Culoare obstacolelor (negru)

# Ceas și variabile
clock = pygame.time.Clock()

# Directorul cu resursele
ASSET_DIR = "assets"

# Încărcare imagine jucător
player_path = os.path.join(ASSET_DIR, "player.png")
player_img = pygame.image.load(player_path)

# Redimensionare imagine jucător
player_width, player_height = 40, 40
player_img = pygame.transform.scale(player_img, (player_width, player_height))

# Poziția inițială a jucătorului
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5  # Viteza jucătorului

# Obstacolele (coordonate și dimensiuni)
obstacles = [
    pygame.Rect(100, 100, 200, 20),  # Obstacol 1
    pygame.Rect(400, 150, 20, 200),  # Obstacol 2
    pygame.Rect(200, 300, 200, 20),  # Obstacol 3
    pygame.Rect(100, 450, 20, 100),  # Obstacol 4
]

# Funcție pentru verificarea coliziunii cu obstacolele
def check_collision(x, y, obstacles):
    player_rect = pygame.Rect(x, y, player_width, player_height)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True  # Coliziune
    return False  # Nu există coliziune

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obține starea tastelor apăsate
    keys = pygame.key.get_pressed()

    # Mișcarea jucătorului
    new_x, new_y = player_x, player_y

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        new_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        new_x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        new_y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        new_y += player_speed

    # Verifică coliziunea cu obstacolele înainte de a schimba poziția
    if not check_collision(new_x, new_y, obstacles):
        player_x, player_y = new_x, new_y

    # Fundal verde ou de rață
    screen.fill(duck_egg_green)

    # Desenăm obstacolele pe ecran
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, obstacle)

    # Afișează jucătorul
    screen.blit(player_img, (player_x, player_y))

    # Actualizează ecranul
    pygame.display.flip()

    # Controlează frame rate-ul
    clock.tick(60)

pygame.quit()
