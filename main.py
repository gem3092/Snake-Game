from turtle import Screen, Turtle

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("The legacy Snake Game")
s.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    for seg in segments:
        seg.fd(20)
