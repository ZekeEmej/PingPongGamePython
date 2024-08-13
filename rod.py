import turtle

class Rod(turtle.Turtle):
    def __init__(self,length,width,initial_position=0,rod_speed=20):
        super().__init__()
        self.shape("square")
        self.shapesize(length,width)
        self.left(90)
        self.color("blue")
        self.penup()
        self.goto(initial_position,0)
        self.speed = rod_speed
    def move_up(self):
        self.forward(self.speed)

    def move_down(self):
        self.backward(self.speed)










if __name__ == "__main__":
    rod = Rod(1,5,400)
    turtle.listen()
    turtle.onkeypress(rod.move_up,"Up")
    turtle.onkeypress(rod.move_down,"Down")

    rod2 = Rod(1,5,-400)
    turtle.onkeypress(rod2.move_up,"w")
    turtle.onkeypress(rod2.move_down,"s")

    turtle.mainloop()

