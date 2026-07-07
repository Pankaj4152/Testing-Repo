import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 70, 50, 50)
player_speed = 7

blocks = []
block_speed = 6
spawn_timer = 0

score = 0

def draw_text(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    player.x = max(0, min(WIDTH - player.width, player.x))

    spawn_timer += 1
    if spawn_timer > 20:
        spawn_timer = 0
        x = random.randint(0, WIDTH - 40)
        blocks.append(pygame.Rect(x, -40, 40, 40))

    for block in blocks[:]:
        block.y += block_speed

        if block.colliderect(player):
            running = False

        if block.y > HEIGHT:
            blocks.remove(block)
            score += 1

    screen.fill((30, 30, 40))

    pygame.draw.rect(screen, (50, 200, 255), player)

    for block in blocks:
        pygame.draw.rect(screen, (255, 80, 80), block)

    draw_text(f"Score: {score}", 10, 10)

    pygame.display.flip()

screen.fill((0, 0, 0))
draw_text("GAME OVER", WIDTH // 2 - 90, HEIGHT // 2 - 20)
draw_text(f"Final Score: {score}", WIDTH // 2 - 100, HEIGHT // 2 + 20)
pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()
