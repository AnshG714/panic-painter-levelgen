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

easy = [pattern1_e, pattern2_e, pattern3_e, pattern4_e, pattern5_e, pattern6_e,
        pattern7_e, pattern8_e, pattern9_e, pattern10_e]

medium = [pattern1_m, pattern2_m, pattern3_m, pattern4_m, pattern5_m, pattern6_m,
        pattern7_m, pattern8_m, pattern9_m, pattern10_m]

hard = [pattern1_h, pattern2_h, pattern3_h, pattern4_h, pattern5_h, pattern6_h]


categories = {
              'e': easy, 
              'm': medium, 
              'h': hard
             }