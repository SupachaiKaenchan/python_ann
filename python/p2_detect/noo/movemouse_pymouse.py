from pymouse import PyMouse

x = 50
y = 50
m = PyMouse()
m.position() #gets mouse current position coordinates
m.move(x,y)
m.click(x,y) #the third argument "1" represents the mouse button
m.press(x,y) #mouse button press
m.release(x,y) #mouse button release