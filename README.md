# Panic Painter level generator

This is the semi-randomized level generator for Panic Painter. Here is a very quick tutorial for how to use the CLI tool.

In this directory, you should run `python loadFile.py` **with the relevant flags**. The flags are listed below:

- `-r` or `--rows`: Specify the number of rows for this level.
  - Default: 10
- `-c` or `--cols`: Specify the number of columns for this level.
  - _The number of columns must be between 3 and 5 inclusive_.
  - Default: 5
- `-d` or `--difficulty`: Specify the difficulty of the level. An easy level will have 1 color/canvas, a medium level will have up to 2 colors/canvas and a hard level will have up to 3 colors/canvas.
  - _The difficulty must be one of `e`, `m` or `h`._
  - Default: 'e'.
- `-l` or `--colors`: Specify the total number of colors in the level.
  - _The number of colors must be between 3 and 5 inclusive_.
  - Default: 4
- `-i` or `--index`: Specify the index of the level.
  - _This argument is necessary_ for writing the output file. Make sure this index is unique for every level. If you generate two levels w the same index and difficulty, files will be overwritten.
- `-o` or `--obstacles`: Specify the number of obstacles in the level.
  - _The number of obstacles must be less than or equal to the number of rows._
  - Default: 0.
  - **Note**: in the output file, an 'obstacle canvas' is depicted as a canvas _ending_ with `10`.
- `-b` or `--beachballs`: Specify the number of beach balls in the level.
  - _The number of beach balls must be less than or equal to the number of rows, and the sum of the portions and the beach balls must ALSO be less than the number of rows._
  - Default: 0.
  - **Note**: in the output file, a beach ball is depicted as a canvas == `[11]`
- `-p` or `--portions`: Specify the number of health portions in the level.
  - _The number of portions must be less than or equal to the number of rows, and the sum of the portions and the beach balls must ALSO be less than the number of rows._
  - Default: 0.
  - **Note**: in the output file, a portion is depicted as a canvas == `[12]`

## Examples

1. Easy level with no obstacles, 10 rows, 5 columns and 4 colors [different representations].

```
# default arguments
python loadFile.py -i 1
```

```
# specify colors
python loadFile.py -i 1 -l 4
```

```
# specify colors, rows
python loadFile.py -i 1 -l 4 -r 10
```

```
# specify colors, rows, columns
python loadFile.py -i 1 -l 4 -r 10 -c 5
```

```
# specify colors, rows, columns, obstacles and difficulty
python loadFile.py -i 1 -l 4 -r 10 -c 5 -d e -o 0
```

2. Hard level with 5 colors, 12 rows and 3 obstacles (in this case, the index is 4 so the output file will be saved as `h4.json`

```
python loadFile.py -i 4 -d h -r 12 -l 5 -o 3
```

3. Medium level with 20 rows (Saved as `m10.json`)

```
python loadFile.py --index 10 --difficulty m --rows 20
```
