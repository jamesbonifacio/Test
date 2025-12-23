import pygame
import random
import sys
from entities import Player, Enemy

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodger")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Fonts
font = pygame.font.SysFont(None, 36)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    player = Player(WIDTH // 2 - 25, HEIGHT - 50)
    enemies = []
    enemy_spawn_timer = 0
    score = 0
    game_over = False

    running = True
    while running:
        clock.tick(FPS)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    # Restart
                    main()
                    return

        if not game_over:
            # Inputs
            keys = pygame.key.get_pressed()
            player.update(keys)

            # Spawning enemies
            enemy_spawn_timer += 1
            if enemy_spawn_timer > 30:  # Spawn every 0.5s approx
                enemy_x = random.randint(0, WIDTH - 30)
                speed = random.randint(3, 7) + (score // 5) # Increase speed with score
                enemies.append(Enemy(enemy_x, -30, speed))
                enemy_spawn_timer = 0

            # Update enemies
            for enemy in enemies[:]:
                enemy.update()
                if enemy.y > HEIGHT:
                    enemies.remove(enemy)
                    score += 1
                
                # Collision check
                if player.rect.colliderect(enemy.rect):
                    game_over = True

        # Drawing
        screen.fill(BLACK)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        
        draw_text(f"Score: {score}", font, WHITE, screen, 10, 10)

        if game_over:
            draw_text("GAME OVER", font, WHITE, screen, WIDTH // 2 - 80, HEIGHT // 2 - 50)
            draw_text("Press 'R' to Restart", font, WHITE, screen, WIDTH // 2 - 110, HEIGHT // 2)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
