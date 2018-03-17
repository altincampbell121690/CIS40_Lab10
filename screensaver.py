import turtle
from random import randint


class PaintBall:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.pensize(7)
        self.Xcord = self.Ycord = 0
        self.Dx = self.Dy = 0
        self.color = ("red", "blue", "green", "orange", "purple", "cyan")
        self.pencolor = ("red", "blue", "green", "orange", "purple", "pink", "light blue", "magenta", "cyan")

    def getxCord(self):
        return self.Xcord

    def getyCord(self):
        return self.Ycord

    def setColor(self, index):
        self.ball.color(self.color[index])

    def setPenColor(self, index):
        self.ball.pencolor(self.pencolor[index])

    def setXdirection(self, xDirection):
        self.Dx = xDirection

    def setYdirection(self, yDirection):
        self.Dy = yDirection

    def lateralBounce(self):
        self.Dx = -self.Dx

    def verticalBounce(self):
        self.Dy = -self.Dy

    def lateralMovement(self):
        self.Xcord += self.Dx

    def verticalMovement(self):
        self.Ycord += self.Dy

    def move(self, x , y):
        self.ball.goto(x,y)


class ScreenSaver:
    def __init__(self):
        self.object = PaintBall()
        xRWall = turtle.window_width() // 2
        xLWall = turtle.window_width() // (-2)
        yTop = turtle.window_height() // 2
        yBtm = turtle.window_height() // (-2)
        self.XwindowTuple = (xLWall, xRWall)
        self.YwindowTuple = (yBtm, yTop)

    def run(self):
        p = 3
        k = r = i = randint(1, 3)
        self.object.setXdirection(p)
        self.object.setYdirection(p)
        while True:
            if r % 15 == 0:
                i = randint(0, 100) % len(self.object.color)
                k = randint(0, 100) % len(self.object.pencolor)
            r += 1
            self.object.setColor(i)
            self.object.setPenColor(k)
            #turtle.fillcolor(color[i])
            #turtle.pencolor(pencolor[k])
            self.object.verticalMovement()
            self.object.lateralMovement()

            if not self.XwindowTuple[0] < self.object.getxCord() < self.XwindowTuple[1]:
                self.object.lateralBounce()
            if not self.YwindowTuple[0] < self.object.getyCord() < self.YwindowTuple[1]:
                self.object.verticalBounce()

            #self.object.goto(self.object.getxCord(), self.object.getyCord())
            self.object.move(self.object.getxCord(), self.object.getyCord())

        turtle.mainloop()



app = ScreenSaver()
app.run()
