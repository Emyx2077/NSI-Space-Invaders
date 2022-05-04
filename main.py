import pygame
from menu import *
from pygame.locals import *
import random
import math

#load mixer and pygame, close mixer et reopen it for fix weird delay issue with sound
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 4, 1024)

#open pygame window
screen = pygame.display.set_mode((720, 720))

#set speed when you keep a touch activate
pygame.key.set_repeat(400, 10)

#read and write best score
def readBestScore():
    txt = open("bestscore", "r")
    score = int(txt.read())
    txt.close()
    return score

def writeBestScore(newScore):
    txt = open("bestscore", "w")
    newScore = str(newScore)
    txt.write(newScore)
    txt.close()

# MAIN BOUCLE
while continuer:

    #menu music
    if menu:
        pygame.mixer.music.load("sounds/musicMenu.ogg")
        pygame.mixer.music.play(-2)

    while menu:

        pygame.display.flip()
        pygame.time.Clock().tick(60)

        #display background and menu button
        screen.blit(background, (0, 0))
        screen.blit(play, (290, 210))
        screen.blit(exit, (295, 390))

        #display best score
        screen.blit(overlayBestScore, (190, 650))
        bestScore = font.render(str(readBestScore()), True, (156, 34, 166))
        screen.blit(bestScore, (440, 660))

        #waiting for event
        for event in pygame.event.get():

            #quit if press close button
            if event.type == QUIT:
                continuer, menu = 0, 0

            #dynamic menu button
            if event.type == MOUSEMOTION:
                if event.pos[0] > 292 and event.pos[0] < 435 and event.pos[1] > 212 and event.pos[1] < 273:
                    survolSound.play()
                    play = button_play_2
                else:
                    play = button_play
                if event.pos[0] > 295 and event.pos[0] < 418 and event.pos[1] > 392 and event.pos[1] < 453:
                    survolSound.play()
                    exit = button_exit_2
                else:
                    exit = button_exit

            #start game if press play button
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 292 and event.pos[0] < 435 and event.pos[1] > 212 and event.pos[1] < 273:
                clickSound.play()
                menu, jouer = 0, 1

            #quit if press exit button
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 295 and event.pos[0] < 418 and event.pos[1] > 392 and event.pos[1] < 453:
                clickSound.play()
                continuer, menu = 0, 0

    #play music
    if jouer:
        pygame.mixer.music.load("sounds/musicJeu.ogg")
        pygame.mixer.music.play(-2)

    while jouer:

        #load background
        screen.blit(background, (0, 0))

        #map border
        if persoX <= 0:
            persoX = 0
        elif persoX >= 596:
            persoX = 596

        #waiting for event
        for event in pygame.event.get():

            #exit
            if event.type == QUIT:
                continuer, jouer = 0, 0

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                jouer, menu = 0, 1
                enemySpawn, score_value, persoX, persoY, laserX, laserY, enemyMax, difficulty_value, speed, fire = 0, 0, 300, 550, 0, 520, 2, 0, 500, False
                enemyX.clear()
                enemyY.clear()

        #control ship
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            persoX += + -5
        elif keys[pygame.K_d]:
            persoX += + 5
        if keys[pygame.K_SPACE]:
            if fire == False:
                laserSound.play()
                fire = True
                laserX = persoX + 35  # +35 just for center sprite

        #laser
        if fire == True:
            screen.blit(laser, (laserX, laserY))
            laserY += + -10
        if laserY < -100:
            fire = False
            laserY = 520

        #enemy
        for i in range(enemyMax):

            pygame.time.Clock().tick(speed)

            #enemey spawn
            if enemySpawn < enemyMax:
                enemySpawn += + 1
                enemyX.append(random.randint(1, 595))
                enemyY.append(random.randint(-120, -90))

            #enemy move
            elif right == True:
                if enemyX[i] < 596:
                   enemyX[i] += + 1

                if enemyX[i] == 596:
                    right, left = False, True

            elif left == True:
                if enemyX[i] > 0:
                    enemyX[i] += + -1
                if enemyX[i] == 0:
                    right, left = True, False

            #collision laser
            hit = math.sqrt(math.pow(enemyX[i] + 28 - laserX, 2) + (math.pow(enemyY[i] - laserY, 2))) #le 28 est là pour centrer l'hitbox sur le vaisseau et non qu'elle sois decentré sur la gauche
            if hit < 35:
                explosionSound.play()
                enemyX[i] = random.randint(1, 595)
                enemyY[i] = random.randint(-120, -90)
                score_value += + 1
                fire = False
                laserY = 520

            #collision forcefield
            proximity = math.sqrt(math.pow(enemyX[i] +28 - persoX, 2) + (math.pow(enemyY[i] - persoY, 2))) #same
            if proximity < 50:
                forcefieldSound.play()
                explosionSound.play()
                screen.blit(forcefield, (persoX, persoY))

                #enemy spawn
                enemyX[i] = random.randint(1, 595)
                enemyY[i] = random.randint(-120, -90)
                score_value += + 1

            #update enemy
            enemyY[i] += + 1
            screen.blit(enemy, (enemyX[i], enemyY[i]))

            #game over
            if enemyY[i] > 700:
                screen.blit(gameover,(0, 0))
                gameoverSound.play()

                # best score?
                if score_value > readBestScore():
                    writeBestScore(score_value)

                #reset
                pygame.mixer.music.fadeout(3000) #freeze aussi la fenetre le temps du fadeout
                enemySpawn, score_value, persoX, persoY, laserX, laserY, enemyMax, difficulty_value, speed, fire = 0, 0, 300, 550, 0, 520, 2, 0, 500, False
                enemyX.clear()
                enemyY.clear()


                jouer, menu = 0, 1
                break

        #increase difficulty
        if score_value == 25 and difficulty_value == 0:
            enemyMax, difficulty_value = 3, 1
            speed += 200
        elif score_value == 50 and difficulty_value == 1:
            enemyMax, difficulty_value = 4, 2
            speed += 300
        elif score_value == 100 and difficulty_value == 2:
            enemyMax, difficulty_value = 5, 3

        #overlay info

        screen.blit(overlayBackground, (0, 0))

        #overlay fire
        if fire == False:
            screen.blit(overlayFire, (305, 669))
        elif fire == True:
            screen.blit(overlayFireDark, (305, 669))

        #overlayScore
        screen.blit(overlayScore, (10, 675))
        score = font.render(str(score_value), True, (221, 148, 150))
        screen.blit(score, (130, 679))

        #overlayDifficulty
        screen.blit(overlayDifficulty, (520, 674))
        difficulty = font.render(str(difficulty_value + 1), True, (221, 148, 150))
        screen.blit(difficulty, (680, 678))

        #refresh main player
        screen.blit(perso, (persoX, persoY))
        pygame.display.update()
