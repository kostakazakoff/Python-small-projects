import random

my_numbers = []
guess_numbers = []
toto_numbers = []
toto_counter = 0
guess_counter = 0

# enter your guess numbers:
print('Enter 6 numbers (from 1 to 49):')
for i in range(6):
    entered_number = int(input('> '))
    my_numbers.append(entered_number)

# generating a 6 random numbers ===========================================
while toto_counter < 6:
    duplication = False
    picked_num = random.randrange(1, 50)

    # to avoid random numbers duplication =================================
    for num in toto_numbers:
        # if it's a duplication, break and generate another one:
        if num == picked_num:
            duplication = True
            break
    # if the number is o.k. append to toto_numbers list and count 1 number:
    if not duplication:
        toto_counter += 1
        toto_numbers.append(picked_num)

# check for hits (comparing my numbers and toto numbers): ==================
for my_num in my_numbers:
    for toto_num in toto_numbers:
        if my_num == toto_num:
            # if there is a hit, append the number to guessed numbers: =====
            guess_numbers.append(my_num)
            guess_counter += 1

print(f'TOTO numbers {toto_numbers}')
print(f'Your numbers {my_numbers}')

# if you guess more than 3 numbers (inclusive), you have a hit: ============
if guess_counter > 2:
    print(f'\nCongratulations! You hit {guess_counter} numbers: {guess_numbers}')
else:
    print('\nSorry. No hits.')
