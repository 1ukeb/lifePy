import sys
import random
import time
import numpy

wid = 100
hei = 27

grid = numpy.random.randint(0,14, size=(hei,wid))

def main():
  for i in range(hei-1):
    for j in range(wid-1):
      if grid[i][j] != 1:
        grid[i][j] = 0

  draw()

  print()
  print('How many iters? ', end='')
  iters = input()
  print(iters)

  for i in range(int(iters)):
    sim()
  
  print()
  input('Any key to exit...')
  exit()

def draw():
  print()
  for row in grid:
    print()
    for val in row:
      p = ' '
      if val == 1:
        p = '0'
      print(p, end='')

def sim():
  for i in range(hei-1):
    for j in range(wid-1):
      iUp = 1
      jUp = 1
      if i == hei:
        iMod = 0
      if j == wid:
        jMod = 0
      iDown = 1
      jDown = 1
      if i == 0:
        iDown = 0
      if j == 0:
        jDown = 0
      
      cout = 0
      cout += grid[i+iUp][j]
      cout += grid[i-iDown][j]
      cout += grid[i][j+jUp]
      cout += grid[i][j-jDown]
      cout += grid[i+iUp][j+jUp]
      cout += grid[i-iDown][j+jUp]
      cout += grid[i+iUp][j-jDown]
      cout += grid[i-iDown][j-jDown]

      if grid[i][j] == 0 and cout == 3:
        grid[i][j] = 1
      elif grid[i][j] == 1 and cout > 3:
        grid[i][j] = 0
      elif grid[i][j] == 1 and cout < 2:
        grid[i][j] = 0

  time.sleep(.050)
  draw()

  

main()