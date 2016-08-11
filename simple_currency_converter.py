#Discription: Convert USD to EU or vice versa

#Find out what the users whants to convert USD->UU or EU->USD

USD = 0.7617 # 1 EU
EU = 1.3812 # 1 USD

def currency_converter():
    user_choice = input("What Do you wont to convert? (1) USD->EU (2) EU->USD \n")

    if user_choice == "1":
        user_usd = input("Enter the amount you wish to convert: ")
        euro = float(user_usd)*USD

        print("{} USD = {} EU".format(user_usd, round(euro, 2)))

    elif user_choice == "2":
        user_eu = input("Enter the amount you wish to convert: ")
        usd = float(user_eu)*EU

        print("{} EU = {} USD".format(user_eu, round(usd, 2)))

    else:
        print("Error incorrect input. Please enter correct data")
        currency_converter()

while True:
    currency_converter()

    user_do_again = input("Would yoy like to convert again? Yes or No \n").lower()

    if user_do_again == 'yes':
        currency_converter()
    else:
        break