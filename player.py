import pygame

class Player:
    def __init__(self, x, y, width, height, speed, color=(0, 0, 255)):
        """Initialize the player object."""
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.color = color

    def move(self, keys, obstacles):
        """Move the player based on key inputs and check for collisions."""
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = self.speed

        # Check for collisions before moving
        new_rect = self.rect.move(dx, dy)
        if not self.check_collision(new_rect, obstacles):
            self.rect = new_rect

    def check_collision(self, new_rect, obstacles):
        """Check if the player collides with any obstacles."""
        for obstacle in obstacles:
            if new_rect.colliderect(obstacle):
                return True
        return False

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the player on the screen.

        :param screen: The surface to draw on.
        :type screen: pygame.Surface
        """
        pygame.draw.rect(screen, self.color, self.rect)
