import random

wList = [
  'dog',
  'mouse',
  'automobile',
  
]
fList = [
  'grape',
  'banana',
  'orange'
]
guesses = 10
guessedL = ''
CurrentWord = ''
wat = input('what type of list do you want to use? Food or random:')
if wat == 'Food':
  what = True
else:
  what = False
  
def wordchoice(what):
  if what == False:
    CurrentWord = random.randint(0, len(wList) - 1)
    return wList[CurrentWord]
  else:
    CurrentWord = random.randint(0, len(fList) - 1)
    return fList[CurrentWord]

word = wordchoice(what)

while guesses > 0:
  count = 0
  
  for char in word:
    if char in guessedL:
      print(char, end="\n")
    else:
      print("_")
      count += 1
    
  if count == 0:
    print(f'Congrats you win!, the word is {word}')
    break
  print()
  guess = input('\n \nWhat letter do you want to guess?:')
  
  guessedL += guess
  
  if guess not in word:
    guesses -= 1
    print('wrong')
    print(f'you have {guesses} guesses left')
  if guesses == 0:
    print('game lost')
