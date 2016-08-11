stock = {'apples': 5, 'orange': 2, 'pears': 0}
already_ate = []

food = input('What food was eaten? ')
person = input('Who ate the food: ')

def menu():
    print('Press 1: To add stock. ')
    print('Press 2: To check stock. ')
    print('Press 3: To enter purchase. ')
    print('Press q: Tp quite the program. ')

    return input('What would like to do? ')

run = menu()
while True:
    if run == '1':
        add_stock = input('Food to be added to the stock? ')
        amount = int(input('Quanity of food to be added to stock? '))
        stock[add_stock] = amount
        run = menu()

    elif run == '2':
        for key, value in stock.items():
            print('{}: {}'.format(key, value))
        run = menu()

    elif run == '3':
        food = input('What food was eaten? ')
        person = input('Who ate the food: ')

        if food in stock:
            if person in already_ate:
                print('{} was sent at the brig'.format(person))
                run = menu()

            else:
                if stock[food] > 0:
                    stock[food] -= 1
                    already_ate.append(person)

                    print('{} ate {}'.format(person, food))
                    run = menu()

                else:
                    print('{} did not eat because we are out of {}'.format(person, food))
                    run = menu()
        else:
            print('{} are out of stock'.format(food))
            run = menu()
    elif run == 'q':
        break

print('Program has end')
