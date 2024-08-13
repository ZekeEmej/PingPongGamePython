#  can you make a class Ball with round shape and size (1,1,), color red
import turtle

class Ball(turtle.Turtle):
    def __init__(self, x,y,speed):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color('red')
        self.penup()
        self.x = x 
        self.y = y
        self.goto(self.x,self.y)
        self.speedx = speed
        self.speedy = speed

    def move(self):
        self.x = self.x + self.speedx
        self.y = self.y + self.speedy
        self.goto(self.x, self.y)
    def bounce(self):
        self.speedy = -self.speedy

    def bounce_x(self):
        self.speedx = -self.speedx

if __name__ == "__main__":
    screen = turtle.Screen()
    ball = Ball(200,0)
    while True:
        ball.move()
        if ball.ycor() >390 or ball.ycor() < -390:
            ball.bounce()
        if ball.xcor() > 390 or ball.xcor() < -390:
            ball.bounce_x()
           
    screen.mainloop()