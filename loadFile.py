from levelgen import constructLevel
import json
import argparse
import random

if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument('-r', '--rows', 
                      type = int, 
                      help = "Number of rows in the game", 
                      default=10)

  parser.add_argument('-c', '--cols', 
                      type = int, 
                      help = "Number of columns in the game", 
                      default = 5,
                      choices = [3,4,5])

  parser.add_argument('-d', '--difficulty',
                      help = "Difficulty of the game (e, m or h)", 
                      default = 'e',
                      choices = ['e','m','h'])

  parser.add_argument('-l', '--colors', 
                      type = int, 
                      help = "Number of colors in the game", 
                      default = 4,
                      choices = [3,4,5])

  parser.add_argument('-i', '--index', 
                      type = int,
                      default = None,
                      help = "The index/uuid of the file. Make sure it's unique, or else it will overwrite some file with the same index")

  parser.add_argument('-o', '--obstacles', 
                      type=int,
                      default=0,
                      help = "The number of obstacles in this level. Make sure this argument is less than the number of rows.")
  args = parser.parse_args()
  level = constructLevel(args.rows, args.cols, args.difficulty, args.obstacles, args.colors)

  colors = [
    [244, 78, 59],
    [251, 158, 0],
    [104, 188, 0],
    [115, 216, 255],
    [250, 40, 255]
  ]

  assert args.index is not None, 'Please provide an index with -i'
  assert args.obstacles <= args.rows, 'Make sure the number of obstacles is less than or equal to the number of rows.'

  random.shuffle(colors)

  colorList = colors[:args.colors]

  if args.difficulty == 'e':
    bg = "museum-bg"
  elif args.difficulty == 'm':
    bg = "city-bg"
  else:
    bg = "space-bg"

  j = {
    'colors': colorList,
    'background': bg,
    'queues': level,
    "timer": { "levelTime": 160, "canvasBaseTime": 10 },
    "version": 1
  }

  with open('output_files/' + args.difficulty + str(args.index) + '.json', 'w') as w:
    json.dump(j, w)
                    

          

            