import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0) 
DARK_GREEN = (0, 150, 0) 

player_img = pygame.image.load('spaceship.png')
player_img = pygame.transform.scale(player_img, (50, 50)) 

player_x = 375 
player_y = 500
player_speed = 0.4 
player_health = 100 

bullet_x = 0 
bullet_y = 500
bullet_width = 10
bullet_height = 15
bullet_speed = 10
bullet_fired = False

alien_img = pygame.image.load('alien.png')
alien_width = 40 
alien_height = 40
alien_img = pygame.transform.scale(alien_img, (alien_width, alien_height)) 

alien_x = random.randint(0, screen.get_width() - alien_width)
alien_y = 50
alien_speed = 0.2 

score = 0
font = pygame.font.Font(None, 32)

base_health = 100 

medkit_img = pygame.Surface((30, 30)) 
medkit_img.fill(DARK_GREEN) 
pygame.draw.rect(medkit_img, WHITE, (10, 0, 10, 30)) 
pygame.draw.rect(medkit_img, WHITE, (0, 10, 30, 10)) 
medkit_x = 0
medkit_y = -50 
medkit_speed = 0.3 
medkit_active = False 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.K_SPACE and not bullet_fired: # Simplified this check
            bullet_x = player_x + 20
            bullet_y = player_y
            bullet_fired = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    
    if keys[pygame.K_SPACE]:
        if not bullet_fired: 
            bullet_x = player_x + 20
            bullet_y = player_y
            bullet_fired = True

    if player_x < 0:
        player_x = 0
    if player_x > screen.get_width() - player_img.get_width():
        player_x = screen.get_width() - player_img.get_width()

    if bullet_fired:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_fired = False
            
    alien_y += alien_speed 
    if alien_y > 600: 
        base_health -= 10 
        if base_health < 0: 
            base_health = 0
        score -= 10 
        if score < 0: 
            score = 0
        
        # New: Heal base health when score reduces
        base_health += 5 # Heal base by 5 points
        if base_health > 100: # Don't go over max base health (100)
            base_health = 100
            
        alien_y = 50 
        alien_x = random.randint(0, screen.get_width() - alien_width)

    if not medkit_active:
        if random.randint(0, 1200) == 0: 
            medkit_active = True
            medkit_x = random.randint(0, screen.get_width() - medkit_img.get_width())
            medkit_y = -medkit_img.get_height() 
    else:
        medkit_y += medkit_speed
        if medkit_y > 600: 
            medkit_active = False 

    bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
    alien_rect = pygame.Rect(alien_x, alien_y, alien_width, alien_height)
    player_rect = pygame.Rect(player_x, player_y, player_img.get_width(), player_img.get_height())
    
    medkit_rect = pygame.Rect(medkit_x, medkit_y, medkit_img.get_width(), medkit_img.get_height())

    if bullet_fired and bullet_rect.colliderect(alien_rect):
        bullet_fired = False
        alien_y = 50 
        alien_x = random.randint(0, screen.get_width() - alien_width)
        score += 1
    
    if player_rect.colliderect(alien_rect):
        player_health -= 10 
        alien_y = 50 
        alien_x = random.randint(0, screen.get_width() - alien_width)
        if player_health < 0:
            player_health = 0

    if medkit_active and player_rect.colliderect(medkit_rect):
        player_health += 20 
        if player_health > 100: 
            player_health = 100
        medkit_active = False 

    screen.fill((0, 0, 0)) 
    
    screen.blit(player_img, (player_x, player_y))

    if bullet_fired:
        pygame.draw.rect(screen, YELLOW, (bullet_x, bullet_y, bullet_width, bullet_height))
    
    screen.blit(alien_img, (alien_x, alien_y))

    if medkit_active:
        screen.blit(medkit_img, (medkit_x, medkit_y))

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.draw.rect(screen, WHITE, (screen.get_width() - 110, 10, 100, 20), 2) 
    pygame.draw.rect(screen, RED, (screen.get_width() - 105, 15, player_health, 10)) 

    pygame.draw.rect(screen, WHITE, (10, 40, 100, 20), 2) 
    pygame.draw.rect(screen, GREEN, (15, 45, base_health, 10)) 

    pygame.display.flip()

pygame.quit()