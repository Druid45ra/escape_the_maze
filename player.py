import pygame

class Player:
    def __init__(self, x, y, width, height, speed, color=(0, 0, 255)):
        """Initialize the player object."""
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.color = color

    def move(self, keys, obstacles):
        """Move the player based on key inputs and check for collisions."""
        dx = -self.speed if (keys[pygame.K_LEFT] or keys[pygame.K_a]) else self.speed if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) else 0
        dy = -self.speed if (keys[pygame.K_UP] or keys[pygame.K_w]) else self.speed if (keys[pygame.K_DOWN] or keys[pygame.K_s]) else 0

        # Check for collisions before moving
        new_rect = self.rect.move(dx, dy)
        if not self.check_collision(new_rect, obstacles):
            self.rect = new_rect

    def check_collision(self, new_rect, obstacles):
        """Check if the player collides with any obstacles."""
        return any(new_rect.colliderect(obstacle) for obstacle in obstacles)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the player on the screen.

        :param screen: The surface to draw on.
        :type screen: pygame.Surface
        """
        screen.fill(self.color, self.rect)
