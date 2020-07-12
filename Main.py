import pygame
import time
import sys
pygame.init()
pygame.font.init()

# load images

dinoWalk = [pygame.image.load('Dino/png/Walk (1).png'), pygame.image.load('Dino/png/Walk (2).png'), pygame.image.load('Dino/png/Walk (3).png'),
            pygame.image.load('Dino/png/Walk (4).png'), pygame.image.load('Dino/png/Walk (5).png'), pygame.image.load('Dino/png/Walk (6).png'),
            pygame.image.load('Dino/png/Walk (7).png'), pygame.image.load('Dino/png/Walk (8).png'), pygame.image.load('Dino/png/Walk (9).png'),
            pygame.image.load('Dino/png/Walk (10).png')]

dinoRun = [pygame.image.load('Dino/png/Run (1).png'), pygame.image.load('Dino/png/Run (2).png'), pygame.image.load('Dino/png/Run (3).png'),
           pygame.image.load('Dino/png/Run (4).png'), pygame.image.load('Dino/png/Run (5).png'), pygame.image.load('Dino/png/Run (6).png'),
           pygame.image.load('Dino/png/Run (7).png'), pygame.image.load('Dino/png/Run (8).png')]

dinoIdle = [pygame.image.load('Dino/png/Idle (1).png'), pygame.image.load('Dino/png/Idle (2).png'), pygame.image.load('Dino/png/Idle (3).png'),
            pygame.image.load('Dino/png/Idle (4).png'), pygame.image.load('Dino/png/Idle (5).png'), pygame.image.load('Dino/png/Idle (6).png'),
            pygame.image.load('Dino/png/Idle (7).png'), pygame.image.load('Dino/png/Idle (8).png'), pygame.image.load('Dino/png/Idle (9).png'),
            pygame.image.load('Dino/png/Idle (10).png')]

dinoDead = [pygame.image.load('Dino/png/Dead (1).png'),  pygame.image.load('Dino/png/Dead (2).png'), pygame.image.load('Dino/png/Dead (3).png'),
            pygame.image.load('Dino/png/Dead (4).png'), pygame.image.load('Dino/png/Dead (5).png'), pygame.image.load('Dino/png/Dead (6).png'),
            pygame.image.load('Dino/png/Dead (7).png'), pygame.image.load('Dino/png/Dead (8).png')]

background = pygame.image.load('download (7).jpg')

walk = [pygame.image.load('Walk (1).png'), pygame.image.load('Walk (2).png'), pygame.image.load('Walk (3).png'),
        pygame.image.load('Walk (4).png'), pygame.image.load('Walk (5).png'), pygame.image.load('Walk (6).png'),
        pygame.image.load('Walk (7).png'), pygame.image.load('Walk (8).png'), pygame.image.load('Walk (9).png'),
        pygame.image.load('Walk (10).png'), pygame.image.load('Walk (11).png'), pygame.image.load('Walk (12).png'),
        pygame.image.load('Walk (13).png'), pygame.image.load('Walk (14).png'), pygame.image.load('Walk (15).png')]

run = (pygame.image.load('Run (1).png'), pygame.image.load('Run (2).png'), pygame.image.load('Run (3).png'),
        pygame.image.load('Run (4).png'), pygame.image.load('Run (5).png'), pygame.image.load('Run (6).png'),
        pygame.image.load('Run (7).png'), pygame.image.load('Run (8).png'), pygame.image.load('Run (9).png'),
        pygame.image.load('Run (10).png'), pygame.image.load('Run (11).png'), pygame.image.load('Run (12).png'),
        pygame.image.load('Run (13).png'), pygame.image.load('Run (14).png'), pygame.image.load('Run (15).png'))

idle = (pygame.image.load('Idle (1).png'), pygame.image.load('Idle (2).png'), pygame.image.load('Idle (3).png'),
        pygame.image.load('Idle (4).png'), pygame.image.load('Idle (5).png'), pygame.image.load('Idle (6).png'),
        pygame.image.load('Idle (7).png'), pygame.image.load('Idle (8).png'), pygame.image.load('Idle (9).png'),
        pygame.image.load('Idle (10).png'), pygame.image.load('Idle (11).png'), pygame.image.load('Idle (12).png'),
        pygame.image.load('Idle (13).png'), pygame.image.load('Idle (14).png'), pygame.image.load('Idle (15).png'))

jump = (pygame.image.load('Jump (1).png'), pygame.image.load('Jump (2).png'), pygame.image.load('Jump (3).png'),
        pygame.image.load('Jump (4).png'), pygame.image.load('Jump (5).png'), pygame.image.load('Jump (6).png'),
        pygame.image.load('Jump (7).png'), pygame.image.load('Jump (8).png'), pygame.image.load('Jump (9).png'),
        pygame.image.load('Jump (10).png'), pygame.image.load('Jump (11).png'), pygame.image.load('Jump (12).png'),
        pygame.image.load('Jump (13).png'), pygame.image.load('Jump (14).png'), pygame.image.load('Jump (15).png'))

dead = (pygame.image.load('Dead (1).png'), pygame.image.load('Dead (2).png'), pygame.image.load('Dead (3).png'),
        pygame.image.load('Dead (4).png'), pygame.image.load('Dead (5).png'), pygame.image.load('Dead (6).png'),
        pygame.image.load('Dead (7).png'), pygame.image.load('Dead (8).png'), pygame.image.load('Dead (9).png'),
        pygame.image.load('Dead (10).png'), pygame.image.load('Dead (11).png'), pygame.image.load('Dead (12).png'),
        pygame.image.load('Dead (13).png'), pygame.image.load('Dead (14).png'), pygame.image.load('Dead (15).png'))

to_draw = pygame.image.load('Idle (1).png')
dino_draw = pygame.image.load('Dino/png/Idle (1).png')

myfont = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiui', 30)
textsurface = myfont.render('Some Text', False, (0, 0, 0))
textx = 560
texty = 0
Width, Height = 1280, 720

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Game')


clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, vel, jump_count, walk_count, jump_control, left, right, count, idle_count, jcount, jumping, running, dead, DeadCount, finished, width, height):
        # place on computer
        self.x = x
        self.y = y
        # moverment speed
        self.vel = 12
        # physics
        self.jump_count = 10
        self.walk_count = 0
        self.jump_control = False
        # user control
        self.left = False
        self.right = False
        # helps with drawing correct
        self.count = 0
        self.idle_count = 0
        self.white = (255, 255, 255)
        self.jcount = jcount
        self.jumping = False
        self.running = False
        self.dead = False
        self.DeadCount = 0
        self.finished = False
        self.width = 287
        self.height = 486

    def PlayerMovement(self):
        self.Physics()
        if not self.dead:
            if not self.running:
                if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                    self.vel = 12
                    self.x -= self.vel
                    self.left = True
                    self.right = False
                elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                    self.vel = 12
                    self.x += self.vel
                    self.right = True
                    self.left = False
                else:
                    self.right = False
                    self.left = False
            if pressed[pygame.K_LSHIFT] and (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]):
                if self.vel == 12:
                    self.vel = self.vel * 5
                self.x += self.vel
                self.right = True
                self.left = False
                self.running = True
            elif pressed[pygame.K_LSHIFT] and (pressed[pygame.K_LEFT] or pressed[pygame.K_a]):
                if self.vel == 12:
                    self.vel = self.vel * 5
                self.x -= self.vel
                self.right = False
                self.left = True
                self.running = True
            else:
                self.running = False
            if pressed[pygame.K_ESCAPE]:
                self.dead = True

    def DeterminePicture(self):
        global to_draw
        if not self.dead:
            if not self.running:
                if self.left:
                    if self.count >= 14:
                        self.count = 0
                    else:
                        self.count += 1
                    self.idle_count = 0
                    to_draw = walk[-self.count]
                if self.right:
                    if self.count >= 14:
                        self.count = 0
                    else:
                        self.count += 1
                    self.idle_count = 0
                to_draw = walk[self.count]
            else:
                if self.left:
                    if self.count >= 14:
                        self.count = 0
                    else:
                        self.count += 1
                    self.idle_count = 0
                    to_draw = run[-self.count]
                if self.right:
                    if self.count >= 14:
                        self.count = 0
                    else:
                        self.count += 1
                    self.idle_count = 0
                    to_draw = run[self.count]

            if not self.left and not self.right:
                if self.idle_count >= 14:
                    self.idle_count = 0
                else:
                    self.idle_count += 1
                to_draw = idle[self.idle_count]
            if self.jumping:
                if self.jcount >= 14:
                    self.jcount = 0
                else:
                    self.jcount += 1
                self.idle_count = 0
                to_draw = jump[p.jcount]
        else:
            if self.DeadCount >= 14:
                self.Showdead()
            else:
                self.DeadCount += 1
            self.idle_count = 0
            to_draw = dead[self.DeadCount]

    def DisplayDead(self):
        global to_draw
        if self.DeadCount >= 14:
            self.Showdead()
        else:
            self.DeadCount += 1
        self.idle_count = 0
        to_draw = dead[self.DeadCount]

    def Showdead(self):
        global textsurface, myfont, textx
        self.dead = True
        textsurface = myfont.render('You died!', True, (0, 0, 0))
        myfont = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiui', 90)
        textsurface = myfont.render('You died!', True, (0, 0, 0))
        textx = 444
        textsurface = myfont.render('You died!', True, (0, 0, 0))
        self.finished = True

    def Physics(self):
        if not self.jumping:
            if pressed[pygame.K_SPACE]:
                self.jumping = True
                self.walk_count = 0
        else:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count > 0:
                    neg = -1
                self.y += (self.jump_count ** 2) * 1.3 * neg
                self.jump_count -= 1
            else:
                self.jumping = False
                self.jump_count = 10


class enemy(object):
    def __init__(self, x, y, count, idlecount, DinoDead, started, width, height, vel, direction, HitEdge, idle):
        self.x = x
        self.y = y
        self.count = 0
        self.idlecount = 0
        self.DeadCount = 0
        self.DinoDead = False
        self.finished = False
        self.started = False
        self.width = 349
        self.height = 420
        self.vel = 10
        self.direction = None
        self.HitEdge = False
        self.idle = True

    def draw(self):
        global dino_draw
        if not self.DinoDead:
            if self.idle:
                if self.idlecount >= 9:
                    self.idlecount = 0
                else:
                    self.idlecount += 1
                dino_draw = dinoIdle[self.idlecount]
            else:
                if self.direction == 'left':
                    if self.count >= 9:
                        self.count = 0
                    else:
                        self.count += 1
                    self.idlecount = 0
                    dino_draw = dinoWalk[self.count]
                else:
                    if self.count >= 9:
                        self.count = 0
                    else:
                        self.count += 1
                    self.idlecount = 0
                    dino_draw = dinoWalk[-self.count]
        else:
            if self.DeadCount >= 7:
                self.ShowDead()
            else:
                self.DeadCount += 1
            self.idlecount = 0
            dino_draw = dinoDead[self.DeadCount]

    def ShowDead(self):
        global textsurface, myfont, textx
        self.DinoDead = True
        textsurface = myfont.render('You Win!', True, (0, 0, 0))
        myfont = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiui', 90)
        textsurface = myfont.render('You Win!', True, (0, 0, 0))
        textx = 444
        textsurface = myfont.render('You Win!', True, (0, 0, 0))
        self.finished = True

    def StartAttack(self):
        self.started = True
        self.direction = 'left'

    def updatex(self):
        self.check_if_hit_wall()
        if self.HitEdge == 'left edge':
            self.direction = 'right'
        elif self.HitEdge == 'right edge':
            self.direction = 'left'
        else:
            self.direction = self.direction
        if self.direction == 'left':
            self.x -= self.vel
        else:
            self.x += self.vel

    def check_if_hit_wall(self):
        if self.x == 0:
            self.HitEdge = 'left edge'
        elif self.x == 1280 - 350:
            self.HitEdge = 'right edge'
        else:
            self.HitEdge = False


class hitbox(object):
    def __init__(self, x, y, color, width, height, placex, placey, rect):
        self.x = x
        self.y = y
        self.colour = color
        self.width = width
        self.height = height
        self.placex = placex
        self.placey = placey
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def Draw(self):
        self.x = self.placex
        self.y = self.placey
        pygame.draw.rect(screen, self.colour, self.rect, 1)


class bullet(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.width = self.radius
        self.goleft = False
        self.goright = False
        self.inMotion = False
        self.offset = 40

    def Fired(self, player):
        self.inMotion = True
        mousex, mousey = pygame.mouse.get_pos()
        if player.x < mousex:
            self.goright = True
            self.goleft = False
        if player.x > mousex:
            self.goright = False
            self.goleft = True

    def Move(self, vel):
        if self.goright:
            self.x += vel
        else:
            self.x -= vel

    def UpdatePosition(self, player):
        if not self.goleft or self.goright:
            self.x = player.x + int((player.width // 2))
            self.y = player.y + (player.height // 2) + self.offset

    def draw(self):
        pygame.draw.circle(screen, (110,144,255), (self.x, self.y), self.radius, self.width)

    def HitWallCheck(self):
        if self.goright:
            if self.x >= Width - self.radius:
                self.inMotion = False
        else:
            if self.x <= 0:
                self.inMotion = False

def RedrawGameWindow(player, Dino, win, bullet):
    # fill background
    # used for hitbox debugging
    win.fill((0, 0, 0))
    # draw hitboxes
    # htiboxes before background to hide them
    pygame.draw.rect(win, PlayerHitbox.colour, pygame.Rect(player.x, player.y, PlayerHitbox.width, PlayerHitbox.height), 1)
    pygame.draw.rect(win, DinoHitbox.colour, pygame.Rect(Dino.x, Dino.y, DinoHitbox.width, DinoHitbox.height), 1)
    pygame.draw.rect(win, (255, 255, 255), pygame.Rect(bullet.x - bullet.radius, bullet.y - bullet.radius, bullet.radius * 2, bullet.radius * 2), 1)
    # background
    # comment out to show hitboxes
    win.blit(background, (0, 0))
    # players/enemies
    # player has to come after dino because of the way pygame processes layers and images
    # dino
    win.blit(dino_draw, (Dino.x, Dino.y))
    # player
    pygame.draw.circle(win, (110, 144, 255), (bullet.x, int(bullet.y)), bullet.radius, bullet.width)
    win.blit(to_draw, (player.x, player.y))
    # text
    win.blit(textsurface, (textx, texty))
    # update everything
    # don't draw images after this line
    pygame.display.update()


def CheckForCollisons(player, Dino):
    PlayerBoxX = player.x + player.width
    DinoBoxX = Dino.x + Dino.width
    PlayerBoxY = player.y + player.height
    DinoBoxy = Dino.y + Dino.height
    if Dino.x in range(int(PlayerBoxX)) and player.x in range(int(DinoBoxX)) and player.y in range(int(DinoBoxy)) and Dino.y in range(int(PlayerBoxY)):
        return True
    else:
        return False


def CheckForEnemyCollisions(Dino, bullet):
    DinoBoxX = Dino.x + Dino.width
    DinoBoxy = Dino.y + Dino.height
    BulletBoxX = bullet.x + bullet.radius
    BulletBoxY = bullet.y + bullet.radius
    if Dino.x in range(int(BulletBoxX)) and bullet.x in range(int(DinoBoxX)) and bullet.y in range(int(DinoBoxy)):
        return True
    else:
        return False

# initialize objects
# bullet
projectile = bullet(200, 200, 30)
# player
p = Player(300, 100, 12, 10, 0, False, False, False, 0, 0, 0, False, False, False, 0, False, 287, 486)
PlayerHitbox = hitbox(p.x, p.y, (255, 255, 255), 286, 486, p.x, p.y, pygame.Rect(p.x, p.y, 286, 486))
# dino(
dino = enemy(720, 200, 0, 0, False, False, 349, 420, 10, None, False, True)
DinoHitbox = hitbox(dino.x, dino.y, (255, 255, 255), 349, 420, dino.x, dino.y, pygame.Rect(dino.x, dino.y, 349, 420))

# used to make the text appear at the right time
StartTime = time.time()
# main loop
while run:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and not projectile.inMotion:
            print('fired')
            projectile.Fired(p)
    try:
        pressed = pygame.key.get_pressed()
    except:
        break
    if dino.started:
        BulletCollison = CheckForEnemyCollisions(dino, projectile)
        if BulletCollison:
            print('dino down')
            dino.ShowDead()
        if dino.finished:
            dino.started = False

    Collision = CheckForCollisons(player=p, Dino=dino)
    if Collision and dino.started:
        print('Collision detected')
        print('ending game')
        break
    # hit wall
    if projectile.inMotion:
        projectile.HitWallCheck()
    # position
    if not projectile.inMotion:
        projectile.goleft = False
        projectile.goright = False
    if projectile.goleft or projectile.goright:
        projectile.Move(45)
    else:
        projectile.UpdatePosition(p)
    # controls
    p.PlayerMovement()
    p.DeterminePicture()
    dino.draw()
    # defines what to draw as text and when
    if dino.started:
        dino.updatex()
    if time.time() - StartTime >= 12 and not dino.started:
        dino.idle = False
        dino.StartAttack()
    elif time.time() - StartTime >= 12 and dino.started and not p.dead:
        textsurface = myfont.render('Goodluck', True, (0, 0, 0))
    else:
        if time.time() - StartTime <= 2 and not p.dead:
            textsurface = myfont.render('Get Ready', True, (0, 0, 0))
            dino.idle = True
        else:
            if not p.dead:
                textsurface = myfont.render(str(time.time() - StartTime), True, (0, 0, 0))
    RedrawGameWindow(p, dino, screen, projectile)
    if p.dead and p.finished:
        time.sleep(4)
        break
    mousex, mousey = pygame.mouse.get_pos()
# second loop to draw dead images
while True:
    try:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                break
        p.DisplayDead()
        RedrawGameWindow(p, dino, screen, projectile)
        if p.finished and p.dead:
            time.sleep(4)
            break
    except:
        print('encountered error, error ignored')
        break

# end game
sys.exit()
