from tealight.logo import move, turn

def whitesquare(side):
  for i in range(0,4):
    move(side)
    turn(90)

turn (-90)

def blacksquare(size):
  
  if size > 300:
    return
  
  move(size)
  turn(90)
  blacksquare(size + 0.5)
  
blacksquare (0)

