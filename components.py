# ============================ DEFINE PATTERNS =================================

# ------------------------ easy patterns ------------------------------

pattern1_e = [
  [[-1], [-1], [-1], [0], [-1]],
  [[0], [0], [0], [1], [0]]
]

pattern2_e = [
  [[-1], [0], [-1], [0], [-1]],
  [[0], [1], [0], [1], [0]]
]

pattern3_e = [
  [[0], [0], [0], [1], [1]]
]

pattern4_e = [
  [[0], [-1], [-1], [-1]],
  [[1], [0], [0], [0]],
  [[2], [1], [1], [1]],
  [[3], [2], [2], [3]]
]

pattern5_e = [
  [[0], [0], [0], [0]]
]

pattern6_e = [
  [[0], [0], [0], [0], [0]]
]

pattern7_e = [
  [[0], [0], [0]]
]

pattern8_e = [
  [[0]],
  [[0]]
]

pattern9_e = [
  [[0], [0]],
  [[0], [0]]
]

pattern10_e = [
  [[0], [1]],
  [[0], [1]]
]

easy_color_cats = {
  1: [pattern5_e, pattern6_e, pattern7_e, pattern8_e, pattern9_e],
  2: [pattern1_e, pattern2_e, pattern3_e, pattern10_e],
  3: [],
  4: [pattern4_e]
}
# ------------------------ medium patterns ------------------------------

pattern1_m = [
  [[0], [0], [-1], [0], [-1]],
  [[1], [1], [0], [1], [0]]
]

pattern2_m = [
  [[0], [0], [-1]],
  [[1], [2], [0]],
  [[1], [3], [1]]
]

pattern3_m = [
  [[0], [0], [0], [1]],
  [[1], [2, 1], [1], [2]]
]

pattern4_m = [
  [[0, 1], [0, 1]],
  [[0], [0]]
]

pattern5_m = [
  [[0, 1], [0, 1]],
  [[0, 1], [0, 1]]
]

pattern6_m = [
  [[0, 1]],
  [[1, 2]],
  [[2, 3]]
]

pattern7_m = [
  [[0, 1], [2, 1]],
  [[2,3], [2, 1]]
]

pattern8_m = [
  [[0, -1], [-1, 0], [-1], [1]],
  [[1], [0], [0], [2]]
]

pattern9_m = [
  [[-1, -1], [-1, -1]],
  [[-1, -1], [-1, -1]]
]

pattern10_m = [
  [[-1, 0]],
  [[0, -1]],
  [[0, 1]]
]

medium_color_cats = {
  1: [pattern9_m],
  2: [pattern1_m, pattern4_m, pattern5_m, pattern10_m],
  3: [pattern3_m, pattern8_m],
  4: [pattern2_m, pattern6_m, pattern7_m]
}

# ------------------------ hard patterns ------------------------------

pattern1_h = [
  [[0], [0], [0], [0]],
  [[1,2,3], [1,2], [2,3], [1,3]]
]

pattern2_h = [
  [[0, 1, 2], [0], [0]],
  [[1], [2, 1, 0], [2]]
]

pattern3_h = [
  [[-1, -1, -1], [-1], [-1, -1, -1]],
  [[-1, -1], [-1], [-1]]
]

pattern4_h = [
  [[-1, -1]],
  [[-1]],
  [[-1, -1, -1]]
]

pattern5_h = [
  [[0, -1], [-1, 1, 2], [1, 0]],
  [[1], [0], [3, 0]]
]

pattern6_h = [
  [[0, 1], [-1, 0, -1]]
]

pattern7_h = [
  [[-1, -1, -1]],
  [[-1]],
  [[-1, -1]]
]

hard_color_cats = {
  1: [pattern3_h, pattern4_h, pattern7_h],
  2: [pattern6_h],
  3: [pattern2_h],
  4: [pattern1_h, pattern5_h]
}

categories = {
  'e': easy_color_cats,
  'm': medium_color_cats,
  'h': hard_color_cats
}

def getComponentsForDifficulty(difficulty, numColors = 4):
  assert difficulty in ['e', 'm', 'h'], 'Invalid difficulty level provided.'
  allComponents = categories[difficulty]
  final = []

  for key in allComponents:
    if key <= numColors:
      final += allComponents[key]

  return final