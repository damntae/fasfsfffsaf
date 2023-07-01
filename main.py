import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("fsafafafasf")
icon = pygame.image.load('resources/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('resources/bg.jpg').convert()
bg = pygame.transform.scale(bg, (400, 200))
walk_r = [
    pygame.image.load('resources/p_r/1.png').convert_alpha(),
    pygame.image.load('resources/p_r/2.png').convert_alpha(),
    pygame.image.load('resources/p_r/3.png').convert_alpha(),
    pygame.image.load('resources/p_r/4.png').convert_alpha(),
]
walk_l = [
    pygame.image.load('resources/p_l/1.png').convert_alpha(),
    pygame.image.load('resources/p_l/2.png').convert_alpha(),
    pygame.image.load('resources/p_l/3.png').convert_alpha(),
    pygame.image.load('resources/p_l/4.png').convert_alpha(),
]

enemy = pygame.image.load('resources/enemy.png').convert_alpha()
enemy = pygame.transform.scale(enemy, (50, 50))

speed = 5
player_x = 150
player_y = 130
count = 0

jump = False
jump_count = 7
bg_x = 0
sound = pygame.mixer.Sound('resources/sound/bg.mp3')
sound.play()

enemyTime = pygame.USEREVENT + 1
pygame.time.set_timer(enemyTime, 2500)

label = pygame.font.Font('resources/font.ttf', 40)
lose_label = label.render('Ты проиграл :(', False, (0, 0, 0))
restart_label = label.render('Продолжить?', False, (0, 0, 0))
restart_labelRect = restart_label.get_rect(topleft=(70, 100))

gameplay = True

enemyig = []

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 400, 0))

    if gameplay:
        player_rect = walk_l[0].get_rect(topleft=(player_x, player_y))

        if enemyig:
            for (i, el) in enumerate(enemyig):
                screen.blit(enemy, el)
                el.x -= 10

                if el.x < -10:
                    enemyig.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            screen.blit(walk_l[count], (player_x, player_y))
        else:
            screen.blit(walk_r[count], (player_x, player_y))


        if keys[pygame.K_a] and player_x > 30:
            player_x -= speed
        elif keys[pygame.K_d] and player_x < 350:
            player_x += speed

        if not jump:
            if keys[pygame.K_w]:
                jump = True
        else:
            if jump_count >= -7:
                if jump_count > 0:
                    player_y -= ((jump_count ** 2)) / 2
                else:
                    player_y += ((jump_count ** 2)) / 2
                jump_count -= 1
            else:
                jump = False
                jump_count = 7



        if count == 3:
            count = 0
        else:
            count += 1

        bg_x -= 2
        if bg_x == -400:
            bg_x = 0
    else:
        screen.fill((255, 255, 255))
        screen.blit(lose_label, (70, 50))
        screen.blit(restart_label, restart_labelRect)

        mouse = pygame.mouse.get_pos()
        if restart_labelRect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            enemyig.clear()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
        if event.type == enemyTime:
            enemyig.append(enemy.get_rect(topleft=(410, 130)))

    clock.tick(10)