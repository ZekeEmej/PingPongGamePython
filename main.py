from ball import Ball 
from rod import Rod
import turtle



turtle.tracer(0)
rod = Rod(1,5,400,rod_speed = 20)
turtle.listen()
turtle.onkeypress(rod.move_up,"Up")
turtle.onkeypress(rod.move_down,"Down")

rod2 = Rod(1,5,-400)
turtle.onkeypress(rod2.move_up,"w")
turtle.onkeypress(rod2.move_down,"s")

ball = Ball(200,0,speed=0.1)

while True:
    ball.move()
    if ball.ycor() >390 or ball.ycor() < -390:
        ball.bounce()
    if rod.distance(ball) < 40 or rod2.distance(ball) < 40:
        ball.bounce_x()

    if ball.xcor() > 390 or ball.xcor() < -390:
        turtle.write("GAME OVER")
        turtle.done()
    turtle.update()
