#############################################################################################
#                                     Statistical Model                                     #
#############################################################################################
def get_statistics(a1, a2, b1, b2, c1, c2):
  import random
  
  a = [ a1, a2 ]
  b = [ b1, b2 ]
  c = [ c1, c2 ]
  
  matrix = [
    [[a[0], a[0], a[0]],
     [a[0], a[0], b[0]],
     [a[0], a[0], b[0]]],
     
    [[b[0], b[0], a[0]],
     [b[0], b[0], b[0]],
     [b[0], b[0], b[0]]],
     
    [[c[0], c[0], a[0]],
     [c[0], c[0], b[0]],
     [c[0], c[0], c[0]]],
  ], [
    [[a[1], a[1], a[1]],
     [a[1], a[1], b[1]],
     [a[1], a[1], b[1]]],
     
    [[b[1], b[1], a[1]],
     [b[1], b[1], b[1]],
     [b[1], b[1], b[1]]],
     
    [[c[1], c[1], a[1]],
     [c[1], c[1], b[1]],
     [c[1], c[1], c[1]]],
  ], [
    [[0.33, 0.33, 0.33],
     [0.33, 0.33, 0.33],
     [0.33, 0.33, 0.33]],
     
    [[0.33, 0.33, 0.33],
     [0.33, 0.33, 0.33],
     [0.33, 0.33, 0.33]],
     
    [[0.33, 0.33, 0.33],
     [0.33, 0.33, 0.33],
     [0.33, 0.33, 0.33]],
  ]
  
  labels           = matrix[0]
  definition       = matrix[1]
  base_probability = matrix[2]
 
  selection_probability = 0.33 * 0.33
  
  row_options = [0, 1, 2]
  col_options = [0, 1, 2]
  arr_options = [0, 1, 2]
  
  cur_row = random.choice(row_options)
  cur_col = random.choice(col_options)
  cur_arr = random.choice(arr_options)
  
  current_label       =      labels[cur_row][cur_col][cur_arr]
  current_description =  definition[cur_row][cur_col][cur_arr]
  
  index_probability = base_probability[cur_row][cur_col][cur_arr]
  current_probability = index_probability * selection_probability
  
  my_data = current_label, current_description, current_probability
  
  spacing = " "
  
  floating_string = str(my_data[2])
  
  print(f"I'm confident it is not [ {current_label} {current_description} ] as it has only {current_probability} probability.")
  
  # Store state between function calls
  with open('data/statistics/labels/current_label.txt', 'w') as f:
      f.write(str(current_label))

  with open('data/statistics/description/current_description.txt', 'w') as f:
      f.write(str(current_label))

  with open('data/statistics/probabilities/current_probability.txt', 'w') as f:
      f.write(str(current_probability))

#############################################################################################
#                                    Reward Structure                                       #
#############################################################################################
def dynamic_reward_allocation():
  import random

  symbol_file = open("data/statistics/labels/current_label.txt")
  description_file = open("data/statistics/description/current_description.txt")

  current_symbol      = symbol_file.read()
  current_probability = float(open("data/statistics/probabilities/current_probability.txt").read())
  
  if current_probability > 0.9999999999999:
    current_probability = 1 / current_probability

  current_description = description_file.read()

  increment = [3, 5, 7]

  for _ in range(random.choice(increment)):
    current_probability = current_probability + 0.015

  current_probability = str(current_probability)

  print("[ :" + current_symbol + ", " + current_description + ", " + current_probability + " ]")
    
  with open('data/statistics/description/current_description.txt', 'w') as f:
      f.write(str(current_description))

  with open('data/statistics/probabilities/current_probability.txt', 'w') as f:
      f.write(str(current_probability))

def dynamic_guilotine_allocation():
  import random

  symbol_file = open("data/statistics/labels/current_label.txt")
  description_file = open("data/statistics/description/current_description.txt")
  
  current_symbol      = symbol_file.read()
  current_probability = float(open("data/statistics/probabilities/current_probability.txt").read())
  
  if current_probability > 0.9999999999999:
    current_probability = 1 / current_probability

  current_description = description_file.read()

  increment = [3, 5, 7]

  for _ in range(random.choice(increment)):
    current_probability = current_probability - 0.15

  current_probability = str(current_probability)

  print("[ :" + current_symbol + ", " + current_description + ", " + current_probability + " ]")
    
  with open('data/statistics/description/current_description.txt', 'w') as f:
      f.write(str(current_description))

  with open('data/statistics/probabilities/current_probability.txt', 'w') as f:
      f.write(str(current_probability))

def proximity_de_medusahoseki(a, b):
  maximum_distance     = b
  distance_probability = a
  
  calculation = maximum_distance - ( maximum_distance * distance_probability )
  calculation = calculation #.round
  
  print("Distance from Medusahoseki: " + f"{calculation}")

def proximity_de_nemedusahoseki(a, b):
  maximum_distance     = b
  distance_probability = 1 - a
  
  calculation = maximum_distance - ( maximum_distance * distance_probability )
  calculation = calculation #.round
  
  print("Distance from Nemedusahoseki ( Salamander Riding Goat ): " + f"{calculation}")

def proximity_de_memorie(a):
  year_period = 12
  
  calculation = 12 - ( 12 * a )
  calculation = calculation #.round
  
  print("this memory was from a prior " + f"{calculation}" + " year period.")
  
#############################################################################################
#                                          Main                                             #
#############################################################################################
symbols      = [                  "cats",                  "dogs",                  "gerbils"]
descriptions = ["are the cleanest pets.", "are mans best friend.", "dont use hamster wheels."]

for _ in range(2):
  get_statistics(symbols[0], descriptions[0],
                 symbols[1], descriptions[1],
                 symbols[2], descriptions[2])

  dynamic_reward_allocation()
  dynamic_guilotine_allocation
  
  current_probability = float(open("data/statistics/probabilities/current_probability.txt").read())
  
  proximity_de_medusahoseki(150, current_probability), proximity_de_memorie(current_probability)
  proximity_de_nemedusahoseki(150, current_probability), proximity_de_memorie(current_probability)
