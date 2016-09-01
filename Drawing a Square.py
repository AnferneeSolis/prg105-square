import turtle

def square(bob,length):
    bob.fd(length)
    bob.lt(90)
    bob.fd(length)
    bob.lt(90)
    bob.fd(length)
    bob.lt(90)
    bob.fd(length)

bob = turtle.Turtle()

square(bob,100)

turtle.done()
