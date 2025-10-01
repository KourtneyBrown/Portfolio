####################################################
# CS 31, Prof. Muldrow
# Name: Kourtney Brown
# Assignment: Project 1
# Due Date: October 1, 2025
####################################################
# prices
    #regular night
#tickets: adult - 11 , child - 3
#food: popcorn - 1.75 , Candy - 1.25 , Water - 2.25 , Floats - 2.75
    #carload night
#tickets: 15 (per car)
#food: popcorn - 2.25 , candy - 1.75 , water - 2.75 , floats - 3.25

date = input('Enter the date (mm/dd/yyyy): ')

night = input('Enter r or R for a regular night, or a c or C for a carload night: ')

#regular night
if night == 'r' or night == 'R':
    adult_tix = float(input('Enter the amount of adult tickets sold: '))
    child_tix = float(input('Enter the amount of child tickets sold: '))
    popcorn = float(input('Enter the amount of popcorn sold: '))
    candy = float(input('Enter the amount of candy sold: '))
    water = float(input('Enter the amount of bottled water sold: '))
    floats = float(input('Enter the amount of root beer floats sold: '))

    adult_tix_calc = adult_tix * 11 #tickets
    child_tix_calc = child_tix * 3

    popcorn_calc = popcorn * 1.75 #food
    candy_calc = candy * 1.25
    water_calc = water * 2.25
    floats_calc = floats * 2.75

    total_tix = adult_tix_calc + child_tix_calc  #child and adult ticket combined
    total = total_tix + popcorn_calc + water_calc + candy_calc + floats_calc #everything
    print()
    print(f'Date: {date} \t\t\t Regular Night')
    print(f'Ticket Sales \t\t\t\t ${total_tix:.2f}') #ticket total
    print(f'Popcorn Sales \t\t\t\t ${popcorn_calc:.2f}')
    print(f'Candy Sales \t\t\t\t ${candy_calc:.2f}')
    print(f'Water Sales \t\t\t\t ${water_calc:.2f}')
    print(f'Float Sales \t\t\t\t ${floats_calc:.2f}')
    print(f'Total Sales \t\t\t\t ${total:.2f}') #everything

#carload night
elif night == 'c' or night == 'C':
    tickets = float(input('Enter the amount of tickets sold: ')) #no child or adult tickets
    popcorn = float(input('Enter the amount of popcorn sold: '))
    candy = float(input('Enter the amount of candy sold: '))
    water = float(input('Enter the amount of bottled water sold: '))
    floats = float(input('Enter the amount of root beer floats sold: '))

    tickets_calc = tickets * 15 #tickets
    popcorn_calc = popcorn * 2.25 # food
    candy_calc = candy * 1.75
    water_calc = water * 2.75
    floats_calc = floats * 3.25
    total = tickets_calc + popcorn_calc + water_calc + candy_calc + floats_calc #everything
    print()
    print(f'Date: {date} \t\t\t Regular Night')
    print(f'Ticket Sales \t\t\t\t ${tickets_calc:.2f}')
    print(f'Popcorn Sales \t\t\t\t ${popcorn_calc:.2f}')
    print(f'Candy Sales \t\t\t\t ${candy_calc:.2f}')
    print(f'Water Sales \t\t\t\t ${water_calc:.2f}')
    print(f'Float Sales \t\t\t\t ${floats_calc:.2f}')
    print(f'Total Sales \t\t\t\t ${total:.2f}')

else:
    print()
    print(f'Date: {date} \t\t\t Regular Night')
    print('Ticket Sales \t\t\t\t $ 0.00')
    print('Popcorn Sales \t\t\t\t $ 0.00')
    print('Candy Sales \t\t\t\t $ 0.00')
    print('Water Sales \t\t\t\t $ 0.00')
    print('Float Sales \t\t\t\t $ 0.00')
    print('Total Sales \t\t\t\t $ 0.00')
