weight = input('enter your weight here sir : ')
number_trial = 1
max_trials = 3
while number_trial <= max_trials:
    units = input('is the weight in kilograms or pounds \n a)kilograms(kgs)    b) pounds(lbs)\n')
    number_trial = number_trial + 1
    if units.lower() == 'b':
        weight_in_kgs = 0.2 * int(weight)
        print(f'your wight is {weight_in_kgs} Kgs, well done')
        break
    elif units.lower() == "a":
        print('your weight sir is ' + weight + ' Kgs  thanks you and try losing a few kilos')
        break
    else:
        print('\n you need to enter a valid answers  check if you have entered the right age or  choose "a" or "b"\n')

else:
    print('\n SORRY!! YOU HAVE EXHAUSTED YOUR TRIAL TRY AGAIN NEXT TIME\n')
print('\n the program was executed properly')


