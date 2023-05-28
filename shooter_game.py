from pygame import *
from random import randint
from time import sleep
from time import time as timer

mixer.init()
font.init()

goal = 100
serdce_aaaai = 0
poka = 0

font1 = font.SysFont(None, 36)

FPS = 120
clock = time.Clock()
game = True

num_fire = 0
rel_flag = False
startReloadTime = timer()

window = display.set_mode((700, 500))
display.set_caption('жоски шутер от 147 лица + злые инопланетяне')
back = transform.scale(image.load('Samsung-Galaxy-S23-Ultra.jpg'), (700, 500))

text_reload = font1.render('Перезарядка', 1, (255, 255, 255))
text_reloadf = font1.render('Перезарядка окончена', 1, (255, 255, 255))

class GameSprite(sprite.Sprite):
    def __init__(self, img, playerx, playery, speed, size_x = 90, size_y = 95):
        super().__init__()
        self.image = transform.scale(image.load(img), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = playerx
        self.rect.y = playery
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

laser = mixer.Sound('laser_blast.ogg')
class Player(GameSprite):
    def update(self):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if pressed_keys[K_d] and self.rect.x < 700 - 83:
            self.rect.x += self.speed
    def fire(self):
            hat_phu.add(Bullet('dart-veider.png', self.rect.centerx, self.rect.top - 20, 10, 15, 20))
            laser.set_volume(0.4)
            laser.play()

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global poka
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(80,620)
            poka += 1
            

hat_phu = sprite.Group()
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

monsters = sprite.Group()
monsters.add(Enemy('ufo.png', 40, 0, 2, 100))
monsters.add(Enemy('ufo.png', 465, 0, 3, 100))
monsters.add(Enemy('ufo.png', 630, 0, 4, 100))
monsters.add(Enemy('ufo.png', 505, 0, 3, 100))
monsters.add(Enemy('ufo.png', 206, 0, 3, 100))


min3uhyy = Player('yourspaceship.png', 350, 405, 6)
mixer.music.load('kazakhstanbomb.mp3')
mixer.music.set_volume(0.4)
mixer.music.play()

while game:
    window.blit(text_reloadf, (300, 400))
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if rel_flag == False:
                    num_fire += 1
                    min3uhyy.fire()
                    if num_fire >= 20:
                        rel_flag = True
                        startReloadTime = timer()

    window.blit(back, (0, 0))

    if rel_flag == True:
        window.blit(text_reload, (300, 400)) 
        if (timer() - startReloadTime) >= 1:
            rel_flag = False
            num_fire = 0

    sprites_list = sprite.groupcollide(hat_phu, monsters, True, True)

    for usual in sprites_list:
        serdce_aaaai += 1
        sp = randint(1,3)
        xcord = randint(80,620)
        monsters.add(Enemy('ufo.png', xcord, 0, sp, 100))

    monsters.update()
    monsters.draw(window)
    hat_phu.update()
    hat_phu.draw(window)
    text_incult = font1.render('Забомбардировались:' + str(serdce_aaaai), 1, (255, 255, 255))
    text_poka = font1.render('Улетели на родину:' + str(poka), 1, (255, 255, 255))
    window.blit(text_incult, (14, 10))    
    window.blit(text_poka, (14, 35))
    min3uhyy.reset()
    min3uhyy.update()


    display.update()
    clock.tick(FPS)