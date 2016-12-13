# Hero 01
from sprites3 import Hero, Obstacle
tilesize = 32

terrain = [[0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,7],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7],
           [0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
           [0,0,0,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,0],
           [0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,6,6,6,0,0],
           [6,9,0,9,9,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0],
           [9,6,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

hero = Hero(8*tilesize, 0)
obstacles = []           

def setup():
    global bg
    bg = loadImage("terrain.png")
    loadObstaclesData()
    frameRate(30)
    size(640, 320)
    hero.loadPics()
    hero.dx = 2
    hero.dy = 2

def draw():
    background(bg)
    hero.move()
    for i in range(len(obstacles)):
        if hero.checkCollision(obstacles[i]):
            if hero.dir == 0:
                hero.x -= hero.dx
            elif hero.dir == 1:
                hero.y -= hero.dy
            elif hero.dir == 2:
                hero.x += hero.dx
            elif hero.dir == 3:
                hero.y += hero.dy
            hero.image1 = hero.image2                            
    hero.display()

def keyPressed():
    if keyPressed and key == CODED:
        if keyCode == RIGHT:
            hero.dir = 0
        elif keyCode == DOWN:
            hero.dir = 1
        elif keyCode == LEFT:
            hero.dir = 2
        elif keyCode == UP:
            hero.dir = 3

def loadObstaclesData():
    for y in range(10):
        for x in range(20):
            if terrain[y][x] > 5:
                obstacles.append(Obstacle(x*tilesize, y*tilesize))