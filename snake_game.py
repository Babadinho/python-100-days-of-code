from turtle import Turtle, Screen
import random
import time

game_is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snakes = []

snake_position = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

screen.listen()


# Add snake
def add_snake(position):
    new_snake = Turtle(shape="square")
    new_snake.color("white")
    new_snake.penup()
    new_snake.goto(position)
    snakes.append(new_snake)


for position in snake_position:
    add_snake(position)


# Extend snake body
def extend():
    add_snake(snakes[-1].position())


def up():
    snakes[0].setheading(90)


def down():
    snakes[0].setheading(270)


def left():
    snakes[0].setheading(180)


def right():
    snakes[0].setheading(0)


screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")


# food.refresh()
def refresh():
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    food.goto(random_x, random_y)


# Snake food
food = Turtle(shape="circle")
food.penup()
food.color("blue")
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.speed("fastest")
refresh()


# Score board
score_board = Turtle()
score_board.score = 0
score_board.color("white")
score_board.penup()
score_board.goto(0, 265)
score_board.hideturtle()


def update_scoreboard():
    score_board.write(f"Score: {score_board.score}", align=ALIGNMENT, font=FONT)


update_scoreboard()


def game_over():
    score_board.goto(0, 0)
    score_board.write("GAME OVER", align=ALIGNMENT, font=FONT)


def increase_score():
    score_board.score += 1
    score_board.clear()
    update_scoreboard()


while game_is_on:
    screen.update()
    time.sleep(0.2)

    for snake in range(len(snakes) - 1, 0, -1):
        new_x = snakes[snake - 1].xcor()
        new_y = snakes[snake - 1].ycor()
        snakes[snake].goto(new_x, new_y)
    snakes[0].forward(MOVE_DISTANCE)

    # Detect collision with food.
    if snakes[0].distance(food) < 15:
        refresh()
        extend()
        increase_score()

    # Detect collision with wall.
    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 or snakes[0].ycor() > 280 or \
            snakes[0].ycor() < -280:
        game_is_on = False
        game_over()

    # Detect collision with tail.
    for segment in snakes[1:]:
        if snakes[0].distance(segment) < 10:
            game_is_on = False
            game_over()

screen.exitonclick()
