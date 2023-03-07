import random
from art import logo, vs
from my_data import data

the_wrong_answer = False
total_score = 0

random_data_2 = random.choice(data)

while not the_wrong_answer:  
   
  random_data_1 = random_data_2
  random_data_2 = random.choice(data)

  while random_data_1 == random_data_2:
    random_data_2 = random.choice(data)
  
  def information(info):
    list_fisrt_info = []
    for elements in info:
      list_fisrt_info.append(info[elements])
    return list_fisrt_info

  first_details = information(info= random_data_1)
  second_details = information(info= random_data_2)

  print(first_details)
  print(second_details)

  if total_score != 0:
    print(f"You're right! Current score: {total_score}")
    
  print(f"Compare A: {first_details[0]}, {first_details[2]}, from {first_details[3]}.")
  print(vs)
  print(f"Against B: {second_details[0]}, {second_details[2]}, from {second_details[3]}.")

  player_choice = input("Who has more followers? Ttpe A or B: ").upper()

  if player_choice == 'A' and first_details[1] > second_details[1]:
    total_score += 1
      
  elif player_choice == 'A' and first_details[1] < second_details[1]:
    print(f"That's wrong! Final score: {total_score}")
    the_wrong_answer = True
      
  elif player_choice == 'B' and second_details[1] > first_details[1]:
    total_score += 1
  elif player_choice == 'B' and second_details[1] < first_details[1]:
    print(f"That's wrong! Final score: {total_score}")
    the_wrong_answer = True
