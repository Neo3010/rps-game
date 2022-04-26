import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
askp = input(
    'What do u choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')
if askp == '0':
  
  print(rock)
elif askp == '1':
  print(paper)
elif askp == '2':
  print(scissors)
comp_random = random.randint(0, 2)
if comp_random == 0:
  print(f'Computer\'s choice: \n{rock}')
elif comp_random == 1:
  print(f'Computer\'s choice: \n{paper}')
elif comp_random == 2:
  print(f'Computer\'s choice: \n{scissors}')
result = ''
if askp == '0':
  if comp_random == 0:
    result += 'It\'s a draw'
  elif comp_random == 1:
    result += 'You lose:('
  elif comp_random == 2:
    result += 'You win!!'
elif askp == '1':
  if comp_random == 0:
    result += 'You win!!'
  elif comp_random == 1:
    result += 'It\'s a draw'
  elif comp_random == 2:
    result += 'You lose:('
elif askp == '2':
  if comp_random == 0:
    result += 'You lose:('
  elif comp_random == 1:
    result += 'You win!!'
  elif comp_random == 2:
    result += 'It\'s a draw'
print(result)