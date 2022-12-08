import pygame as py
import sys
import time

# initialize the pygame modules.
py.init()

# define the color black in rgb.
black = 0, 0, 0
# define the variable speed as an array.
speed = [2, 2]


# define the size of the display.
size = width, height = 960, 540
# create a display of given "size".
Display = py.display.set_mode(size)


# define the variable ball as a surface with the same pixels as said image.
ball = py.image.load("blueray.png")
# define the variable ballobjc as a rect object(a rectangle) of surface "ball".
ballobjc = ball.get_rect()


# create a contineous loop that says if the event given by the function "py.event.get()" is "py.QUIT", run "sys.exit()" which will quite the application.
while True:
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()


    # redefine "ballobjc" with the method "move", which creates a copy of said object, except moved a certain # of pixels in the x and y, given by the array "speed".   
    ballobjc =  ballobjc.move(speed)


    # this checks if the left edge of "ballobjc" is below position 0 or if the right edge is to the right of the width of the display.
    # if this is true, the array speed has its first entry multiplied by -1, effectively reversing the direction it will travel on the x axis during the following loops.
    if ballobjc.left < 0 or ballobjc.right > width:
        speed[0] = -speed[0]
    # this is the same thing but for the y axis. Also note that the second entry of array speed is changed.
    if ballobjc.top < 0 or ballobjc.bottom > height:
        speed[1] = -speed[1]  

    # this function just makes the screen black. This is important because we are running an animation. 
    # if the screen is not reset after each frame then as the object moves it will leave a trail behind it.      
    Display.fill(black)

    # this copies the pixels from from surface "ball" and area "ballobjc" onto the display.
    Display.blit(ball, ballobjc)
    # this function reveals the display to the player. 
    # pygame uses this buffer of copying to display and then revealing the display to prevent the player from seeing the unfinished frames of the display.
    py.display.flip()

    # this function just slows the while loop down to about 30fps.
    time.sleep(1/30)