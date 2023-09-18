import random
user_birthday = int(input("Enter birthday as integer: "))
num_people = int(input("How many people o you want in the simulation:"))
num_sims = 1000
num_correct_sims = 0
same = 0
for i in range(num_sims):
  for i in range(num_people):
    #sim_birthday = int(input("Enter birthday as integer: "))
    sim_birthday = random.randint(1,366)
    if user_birthday == sim_birthday:
      same += 1
print(f"out of the {num_sims} simulations that we did, {same} people had the same birthday as you!")
percent = same / num_people * 10
print(f"The probability of someone having the same birthday as you is {percent}%")
