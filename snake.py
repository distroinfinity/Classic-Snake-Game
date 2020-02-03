import turtle
import time
import random 

delay = 0.1
score = 0
hscore_file = open('highscore.txt','r')
high_score_string = hscore_file.read()
hscore_file.close()
high_score = int(high_score_string)
new_high_score = high_score

#set up a screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0) #turns off the screen update


#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("bisque")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("tomato")
food.penup()
food.goto(0,50)

#Snake body
tail = []


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("whitesmoke")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center",font=("Courier", 24, "normal"))


  
# Functions
def go_up():
    if head.direction != "down" :
        head.direction = "up"
def go_down():
    if head.direction!= "up" :
        head.direction = "down"
def go_left():
    if head.direction!= "right" :
        head.direction = "left"
def go_right():
    if head.direction!= "left" :
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

     
# Keboard binding
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
        
# Main game loop
while True:
    window.update()

    #Check for collision with food 
    if head.distance(food) < 20 :
        food.setx(random.randint(-290,290)) 
        food.sety(random.randint(-290,290))

        new_tail = turtle.Turtle()
        new_tail.shape("circle")
        new_tail.color("sandybrown")
        new_tail.speed(0)
        new_tail.penup()
        tail.append(new_tail)

        #Shorten the delay
        delay -=.002
          
        # Increase the score
        score +=10
        if score > int(high_score):
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
        

    for i in range(len(tail)-1, 0, -1):
        tail[i].goto(tail[i-1].xcor(), tail[i-1].ycor())

    if len(tail) > 0:
        tail[0].goto(head.xcor(), head.ycor())

    move()

    
    # Check for collisions
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        # Hide tail part
        for j in tail:
            j.goto(1000,1000) #some random point of the screen
        # Clear Tail
        tail.clear()
        #Reset delay
        delay = 0.1
        
        #Reset score
        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    for i in tail:
        if i.distance(head) == 0 :
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            for j in tail:
                j.goto(1000,1000) #some random point of the screen
            # Clear tail 
            tail.clear()

            #Reset delay
            delay = 0.1
        
            #Reset score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
            
    time.sleep(delay)   #stops the program for 1/10 of a sec
    if(new_high_score < high_score):
        new_high_score = high_score
        hscore_file2 = open('highscore.txt','w')
        hscore_file2.write(str(new_high_score))
        hscore_file2.close()



window.mainloop()
