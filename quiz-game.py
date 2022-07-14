print("Welcome to my quiz game")
print('This quiz comprises of ten (10) questions in which one (1) point is allocated to each question.')
print('your final score will be displayed after the quiz to see how you fair.')

playing = input("Do you want to play? ").lower()
if playing == 'yes':
    print("Yes! let's play")
elif playing == 'no':
    print("Oops! Have a nice day")
    quit()
else:
    print("Invalid input, Type 'yes' or 'no' to play")
    quit()
score = 0
Answer = input('Which country has the largest land mass in the world? ').lower()
if Answer == "russia":
    print('Correct!')
    score += 1
else:
    print('Oops! You missed')
Answer1 = input('Which city is the most populous in Africa? ').lower()
if Answer1 == "kinshasa":
    print('Correct!')
    score += 1
else:
    print('Oops! You missed')
Answer2 = input('Which city has the most skyscrapers? ').lower()
if Answer2 == "hong kong":
    print('Correct!')
    score += 1
else:
    print('Oops! You missed')
Answer3 = input('What is the capital of Mauritius? ').lower()
if Answer3 == "port louis":
    print('Correct!')
    score += 1
else:
    print('Oops! You missed')
Answer4 = input('The fastest land animal is? ').lower()
if Answer4 == "cheetah":
    print('Correct!')
    score += 1
else:
    print('Oops! You missed')
Answer5 = input('What did Alexander Graham bell invented? ').lower()
if Answer5 == "telephone":
    print('Correct!')
    score += 1
else:
    print('Oops! You missed')
Answer6 = input('What does CPU stands for? ').lower()
if Answer6 == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Oops! You missed')
Answer7 = input('Which country is popularly related with mummies? ').lower()
if Answer7 == "egypt":
    print('Correct!')
    score += 1
else:
    print('Oops! You missed')
Answer8 = input('how many letters is in the english alphabet? ').lower()
if Answer8 == "26":
    print('Correct!')
    score += 1
else:
    print('Oops! You missed')
Answer9 = input('The last letter of the english alphabet is? ').lower()
if Answer9 == "z":
    print('Correct!')
    score += 1
else:
    print('Oops! You missed')

print(f'Kudos! you scored {score} out of 10 ')
