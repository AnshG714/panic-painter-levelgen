""" A naive level generation algorithm for Panic Painter. 

  Assumptions:
  - Minimum number of colors: 3
  - Maximum number of colors: 5
  - mininum number of columns: 3
  - maximum number of columns: 5

  Note that in this case, the easy/medium/hard distinctions are SOLELY based on 
  the max number of colors each canvas needs, i.e., 1->easy; 2->medium; 3->hard.

  The team has to decide the 'canvas base time' too, which can be used to alter
  level difficuly. An easy level can be made harder and vice versa simply by 
  altering the level timer.
"""
import numpy as np # for easier matrix construction.
import random
import math

from components import categories

def prettyprint(c):
  """A helper function to aid pretty printing

  Args:
      c (Object[]): Prints c in a row-by-row manner, making it a bit easier to 
      read. Meant for 2+ - dimensional arrays. 
  """
  for r in c:
    print(r)

def assignSubmatrix(mat1, mat2, i, j):
  """Assigns submatrix mat2 in mat1, with the TOP LEFT entry of mat2 starting 
  at entry i,j of mat1. This operation modifies mat1.

  Args:
      mat1 ([Object[]]): The main matrix to modify
      mat2 ([Object[]]): The submatrix
      i (int): The axis-0 index of mat1 to start mat2 assignment
      j (int): The axis-1 index of mat1 to start mat2 assignment
  """
  x = i - (len(mat2) - 1)
  x2 = 0
  while x2 < len(mat2):
    y = 0
    while y < len(mat2[0]):
      mat1[x][y + j] = mat2[x2][y]
      y += 1
    x += 1
    x2 += 1
  return mat1

def chooseComponent(maxWidth, currRow, maxRows, difficulty):
  """Select a component for a given difficulty, with a maximum width and one that 
  fits within the canvas.

  Args:
      maxWidth (int): The maximum width this component can take on.
      currRow (int): The row the BOTTOM of the component will be placed on.
      maxRows (int) The maximum number of rows for this level.
      difficulty (char): The difficulty level

  Returns:
      The component to add.
  """
  components = categories[difficulty]
  candidates = []
  for component in components:

    if len(component[0]) <= maxWidth and currRow - (len(component) - 1) >= 0:
      candidates.append(component)
  
  if candidates == []:
    return None

  candidates.sort(key = lambda x : len(x))

  component = random.choice(candidates)

  # shuffle colors around to prevent 'zero-overloading'
  colorMap = [0, 1, 2, 3]
  random.shuffle(colorMap)

  for row in component:
    for col in row:
      for i in range(len(col)):
        if col[i] != -1:
          col[i] = colorMap[col[i]]

  return component

def fillRandomEntries(block):
  colors = [0,1,2,3]
  s = set(colors)
  randomColorPresent = False
  for color in block:
    if color != -1:
      s.remove(color)
    else:
      randomColorPresent = True

  if not randomColorPresent:
    return
  
  # I convert this back to a list and shuffle instead of directly calling 's.pop' 
  # because the implementation of sets in python always ends up returning 0 or 1 
  # due to hashing.
  remainingColors = list(s)
  random.shuffle(remainingColors)
  for i in range(len(block)):
    if block[i] == -1:
      block[i] = remainingColors.pop()

def constructLevel(numRows, numColumns, difficulty):
  assert (3 <= numColumns <= 5)
  assert (difficulty in ['e', 'm', 'h'])

  #canvas = np.full((numRows, numColumns), [])
  canvas = [[[] for _ in range(numColumns)] for _ in range(numRows)]
  currRow = numRows - 1

  # >>>> Phase 1 of Algorithm: Try to fit as much of the grid with the given components as possible
  while currRow >= 0:
    currCol = 0
    while currCol < numColumns:
      # find the correct span width to fill
      j = currCol

      while j < numColumns and canvas[currRow][j] == []:
        j += 1

      maxWidth = j - currCol

      if maxWidth == 0:
        currCol += 1
      else:
        randomComponent = chooseComponent(maxWidth, currRow, numRows, difficulty)
        if not randomComponent:
          currCol += 1
        else:
          assignSubmatrix(canvas, randomComponent, currRow, currCol)
          currCol += len(randomComponent[0])

    currRow -= 1

  # >>>> Phase 2 of algorithm: fill any 
  for row in canvas:
    for col in row:
      if col == []:
        # fill with random element. 
        if difficulty == 'e':
          col.append(-1)
        elif difficulty == 'm':
          numColors = random.choice([1,2])
          col += [-1] * numColors
        else:
          numColors = random.choice([1,2,3])
          col += [-1] * numColors

  # >>>> Phase 3 of algorithm: switch out the random colors. 
  for row in canvas:
    for c in row:
      fillRandomEntries(c)

  return canvas 