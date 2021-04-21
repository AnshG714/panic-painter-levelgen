from levelgen import constructLevel
import json
import argparse
import random

if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument('-r', '--rows', 
                      type=int, 
                      help = "Number of rows in the game", 
                      default=10)

  parser.add_argument('-c', '--cols', 
                      type=int, 
                      help = "Number of columns in the game", 
                      default=5,
                      choices=[3,4,5])

  parser.add_argument('-d', '--difficulty',
                      help = "Difficulty of the game (e, m or h)", 
                      default='e',
                      choices=['e','m','h'])

  parser.add_argument('-l', '--colors', 
                      type=int, 
                      help = "Number of colors in the game", 
                      default=4,
                      choices=[3,4,5])

  parser.add_argument('-i', '--index', 
                      type = int,
                      default = None,
                      help = "The index/uuid of the file. Make sure it's unique, or else it will overwrite some file with the same index")
  args = parser.parse_args()
  level = constructLevel(args.rows, args.cols, args.difficulty, args.colors)

  colors = [
    [244, 78, 59],
    [251, 158, 0],
    [104, 188, 0],
    [115, 216, 255],
    [250, 40, 255]
  ]

  assert args.index, 'Please provide an index with -i'

  random.shuffle(colors)

  colorList = colors[:args.colors]

  j = {
    'colors': colorList,
    'background': 'bg-color2',
    'queues': level,
    "timer": { "levelTime": 160, "canvasBaseTime": 10 },
    "version": 1
  }

  with open('output_files/' + args.difficulty + str(args.index) + '.json', 'w') as w:
    json.dump(j, w)
                    

          

            