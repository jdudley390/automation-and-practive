import random
import turtle as t 

t.bgcolor('yellow')
#create a turtle for the caterpillar game, make the shape just a red square start speed at 0
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
#use pen up to contol turtle without make line and hide the turtle
caterpillar.penup()
caterpillar.hideturtle()

#create a seperate turtle to draw the leaves
leaf = t.Turtle()
#set coordinates for leaf shape
leaf_shape = ((0,0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 4))
#t.register_shape allows you to name(leaf) and create your own shape using coordinates(leaf_shape). this shape can them be passed to t.shape
t.register_shape('leaf', leaf_shape)
#pass the string 'leaf'(created in t.ragister_shape) to the shape function t.shape
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

#create text to instruct player to start the game. When the game has not started this screen comes up
game_started = False
#create turtle for text
text_turtle = t.Turtle()
#write with turtle using. align it to the center of the screen
text_turtle.write("Press SPACE to begin", align='center', font=('Arial', 16, 'bold'))
text_turtle.hideturtle()

#create a turtle to write score
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

#turtle windo is 400x400 xAxis(-200, 200), yAxis(-200, 200)
def outside_window():
    #take the full window width and divide by 2 to get distance from center. These will be the wall
    #t.window_width and t.window_height return width and height of screen
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    #return the turtles position
    (x, y) = caterpillar.pos()
    #if turtle is ouside the walls return outside variable. If turtle is outside outside_window function will be called in main code
    #outside_window function then calls game_over function
    outside = \
            x < left_wall or \
            x > right_wall or \
            y < bottom_wall or \
            y > top_wall
    return outside

def game_over():
    #make everything yellow like the background
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    #use first turtle to write game over
    t.write('Game Over!', align='center', font=('Arial', 30, 'bold'))

def display_score(current_score):
    #Display score in the top right corner
    #this function only displays the score. score keeping is done in the main funcion loop
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    #set turtle to x, y coordinates
    score_turtle.setpos(x, y)
    #display the score as a string
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'normal'))
def place_leaf():
    #ht and st are short for hide and show turtle
    leaf.ht()
    #choose random coordinates for leaf to appear
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st()


def start_game():
    #bring in game_started variable which has been set to false
    #when the game has started. This is the beginning of the game
    global game_started
    if game_started:
        return
    game_started = True
    #start score at 0 and clear text from text_turtle from screen. score_turtle will remain
    score = 0
    text_turtle.clear()
    #create accumulator for caterpillar speed, and change the shape of the turtle
    caterpillar_speed = 2
    caterpillar_length = 3
    #shapesize parameters: stretch_wid is stretchfactor perpendicular to its orientation (1)
    ##stretch_len is stretchfactor in direction of its orientation (caterpillar_length)
    ##outline determines the width of the shapes’s outline (1)
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    #Call the display score function to display 0 and the place_leaf function to place the first leaf
    display_score(score)
    place_leaf()

    while True:
        #move caterpillar forward and have it eat a leaf if it's within 20 pixels
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            #add 1 to caterpillars lenght and recall the shapesize method to increase the caterpillars size. increase speed by 1 too
            caterpillar_length += 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 1
            #add 10 to score and recall display score to show the added points
            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break
def move_up():
    #first line checks if caterpillar is moving left or right
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)
def move_down():
    #first line checks if caterpillar is moving left or right
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)
def move_left():
    #first line checks if caterpillar is moving up and down
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)
def move_right():
    #first line checks if caterpillar is moving up and sown
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)
#use onkey method to tie the space bar to the start game function
#when you press SPACE the game will start with start_game being called
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')
#t.listen allows the program to recieve signals from the keyboard
t.listen()
#t.mainloop Starts event loop - calling Tkinter’s mainloop function
t.mainloop

