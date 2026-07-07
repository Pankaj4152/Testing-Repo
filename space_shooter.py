
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Space Shooter")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (20, 20, 30)
GREEN = (0, 255, 0)
RED = (255, 60, 60)

player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 70, 50, 50)
bullets = []
enemies = []

font = pygame.font.SysFont(None, 36)

score = 0
enemy_timer = 0

running = True

while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx - 3, player.y, 6, 15))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 7
    if keys[pygame.K_RIGHT]:
        player.x += 7

    player.x = max(0, min(WIDTH - player.width, player.x))

    enemy_timer += 1
    if enemy_timer > 25:
        enemy_timer = 0
        enemies.append(pygame.Rect(random.randint(0, WIDTH - 40), -40, 40, 40))

    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.bottom < 0:
            bullets.remove(bullet)

    for enemy in enemies[:]:
        enemy.y += 4

        if enemy.top > HEIGHT:
            enemies.remove(enemy)
            continue

        if enemy.colliderect(player):
            running = False

        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                if enemy in enemies:
                    enemies.remove(enemy)
                if bullet in bullets:
                    bullets.remove(bullet)
                score += 1
                break

    pygame.draw.rect(screen, GREEN, player)

    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
