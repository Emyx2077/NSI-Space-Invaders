import pygame

pygame.init()

#menu
button_play = pygame.image.load("images/play.png")
button_play_2 = pygame.image.load("images/play_2.png")
button_credit = pygame.image.load("images/credit.png")
button_credit_2 = pygame.image.load("images/credit_2.png")
button_exit = pygame.image.load("images/exit.png")
button_exit_2 = pygame.image.load("images/exit_2.png")

play = button_play
credit = button_credit
exit = button_exit

#sound
forcefieldSound = pygame.mixer.Sound("sounds/forcefield.wav")
laserSound = pygame.mixer.Sound("sounds/laser.wav")
gameoverSound = pygame.mixer.Sound("sounds/gameover.wav")
explosionSound = pygame.mixer.Sound("sounds/explosion.wav")
survolSound = pygame.mixer.Sound("sounds/survol.wav")
clickSound = pygame.mixer.Sound("sounds/click.wav")

#overlay
overlayFire = pygame.image.load("images/fire.png")
overlayFireDark = pygame.image.load("images/fireDark.png")
overlayScore = pygame.image.load("images/score.png")
overlayDifficulty = pygame.image.load("images/difficulty.png")
overlayBackground = pygame.image.load("images/backgroundOverlay.png")
overlayBestScore = pygame.image.load("images/bestScore.png")

#random things
icone = pygame.image.load("images/icone.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Space Invaders")
credit_texte = 'credit'
speed = 500
continuer = 1
jouer = 0
menu = 1

#background
background = pygame.image.load("images/background.jpg")

#load player's starship
perso = pygame.image.load("images/perso.png")
persoX = 300
persoY = 550

#forcefield
forcefield = pygame.image.load("images/forcefield.png")

#load laser
laser = pygame.image.load("images/laser.png")
laserX = 0
laserY = 520
fire = False

#load enemy
enemy = pygame.image.load("images/enemy.png")
enemyX = []
enemyY = []
enemySpawn = 0
enemyMax = 2
right = True
left = False

#score and difficulty
score_value = 0
font = pygame.font.SysFont('comicsansms', 32)
difficulty_value = 0

#gameover
gameover = pygame.image.load("images/gameover.png")