import turtle


def drawCircle (centerpoint, radius):

    (x,y) = centerpoint

    turtle.up()

    turtle.setpos(x,y)

    # turtle.right(3) this is kind of pointless

    turtle.down()
    turtle.delay(0)
    turtle.circle(radius)

    print "Radius is", radius

    print "The circumference moved is", (2.0 * 3.14 * radius)



drawCircle((20,20), 20)
