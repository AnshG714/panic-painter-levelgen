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
import random
import math

from components import getComponentsForDifficulty

def prettyprint(c):
  """A helper function to aid pretty printing

  Args:
      c (Object[]): Prints c in a row-by-row manner, making it a bit easier to 
      read. Meant for 2+ - dimensional arrays. 
  """
  for r in c:
    print(r)

def assignSubmatrix(mat1, mat2, i, j):
  """Assigns submatrix mat2 in mat1, with the BOTTOM LEFT entry of mat2 starting 
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

def chooseComponent(components, maxWidth, currRow, maxRows, difficulty, numColors):
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
  candidates = []
  for component in components:

    if len(component[0]) <= maxWidth and currRow - (len(component) - 1) >= 0:
      candidates.append(component)
  
  if candidates == []:
    return None

  candidates.sort(key = lambda x : len(x))

  component = random.choice(candidates)

  # shuffle colors around to prevent 'zero-overloading'
  colorMap = [i for i in range(numColors)]
  random.shuffle(colorMap)
  for row in component:
    for col in row:
      for i in range(len(col)):
        if col[i] != -1:
          col[i] = colorMap[col[i]]

  return component

def fillRandomEntries(block, numColors):
  colors = [i for i in range(numColors)]
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

def transform(l1):
  l2 = []
  # iterate over list l1 to the length of an item
  for i in range(len(l1[0])):
      # print(i)
      row =[]
      for item in l1:
          # appending to new list with values and index positions
          # i contains index position and item contains values
          row.append(item[i])
      l2.append(row)

  for el in l2:
    el.reverse()
  return l2

def constructLevel(numRows, 
                  numColumns, 
                  difficulty, 
                  numObstacles, 
                  numHealthPortions,
                  numBeachBalls,
                  numColors = 4):

  # note - a canvas with [10] is an obstacle!

  assert (3 <= numColumns <= 5)
  assert (difficulty in ['e', 'm', 'h'])
  assert numBeachBalls + numHealthPortions <= numRows, "The sum of beach balls and health portions cannot exceed the number of rows since beach balls and health portions cannot be in the same row."

  canvas = [[[] for _ in range(numColumns)] for _ in range(numRows)]
  currRow = numRows - 1
  components = getComponentsForDifficulty(difficulty, numColors)
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
        randomComponent = chooseComponent(components, maxWidth, currRow, numRows, difficulty, numColors)
        if not randomComponent:
          currCol += 1
        else:
          assignSubmatrix(canvas, randomComponent, currRow, currCol)
          currCol += len(randomComponent[0])

    currRow -= 1

  # >>>> Phase 2 of algorithm: fill any empty arrays (which represent cells that 
  # couldn't be filled.)
  for row in canvas:
    for col in row:
      if col == []:
        # fill with random element. 
        if difficulty == 'e':
          col.append(-1)
        elif difficulty == 'm':
          colorsOnCanvas = random.choice([1,2])
          col += [-1] * colorsOnCanvas
        else:
          colorsOnCanvas = random.choice([1,2,3])
          col += [-1] * colorsOnCanvas

  # >>>> Phase 3 of algorithm: switch out the random colors. 
  for row in canvas:
    for c in row:
      fillRandomEntries(c, numColors)

  # >>>> Phase 4 of algorithm: switch out components for bombs, health portions and beach balls.

  # obstacle: ending with a 10
  # beach ball: 11
  # health portion: 12
  obstacleRows = random.sample(range(numRows), numObstacles)
  obstacleColumns = random.choices(range(numColumns), k=numObstacles)
  obstaclesCoords = zip(obstacleRows, obstacleColumns)
  for x, y in obstaclesCoords:
    canvas[x][y] = canvas[x][y][:] + [10] # this is funky but needed because of weird array memory references.

  # Note that we can guarantee a spot for health portions/beach balls 
  beachBallRows = random.sample(range(numRows), numBeachBalls)
  portionRowSet = set(range(1, numRows)).difference(set(beachBallRows))
  portionRows = random.sample(portionRowSet, numHealthPortions)

  for r in beachBallRows:
    possibleCols = []
    for c in range(numColumns):
      if canvas[r][c][-1] != 10:
        possibleCols.append(c)

    chosenCol = random.choice(possibleCols)
    canvas[r][chosenCol] = [11]


  for r in portionRows:
    possibleCols = []
    for c in range(numColumns):
      if canvas[r][c][-1] != 10:
        possibleCols.append(c)

    chosenCol = random.choice(possibleCols)
    canvas[r][chosenCol] = [12]

  return transform(canvas)