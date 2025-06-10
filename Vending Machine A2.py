#Code for the Menu that defines the menu items
menus = {
    "DrinksMenu": {
        "D1" :{"item": "Water","Price": 2,"Stock": 11},
        "D2" :{"item": "Cola","Price": 2.50,"Stock": 7},
        "D3" :{"item": "Fanta","Price": 2.50,"Stock": 4},
        "D4" :{"item": "Cold Coffee","Price": 8,"Stock": 2},
        "D5" :{"item": "Gatorade","Price": 7,"Stock": 8},
    },
    "InstantFoodMenu": {
        "I1" :{"item": "NissinCupNoodle","Price": 4,"Stock": 6},
        "I2" :{"item": "IndomieCupNoodle","Price": 5.50,"Stock": 7},
        "I3" :{"item": "SamyangBuldak","Price": 5.90,"Stock": 8},
        "I4" :{"item": "KnorrSoup","Price": 6,"Stock": 5},
        "I5" :{"item": "Sandwiches","Price": 8,"Stock": 0},
    },
    "ChipsMenu": {
        "S1" :{"item": "Doritos","Price": 3,"Stock": 3},
        "S2" :{"item": "Cheetos","Price": 3.50,"Stock": 2},
        "S3" :{"item": "Lays","Price": 4,"Stock": 6},
        "S4" :{"item": "Pringles","Price": 6,"Stock": 4},
        "S5" :{"item": "Ruffles","Price": 4,"Stock": 7},
    },
    "SnacksMenu": {
        "SN1" :{"item": "OreoCookies","Price": 4.50,"Stock": 6},
        "SN2" :{"item": "ChipsAhoyCookies","Price": 5,"Stock": 8},
        "SN3" :{"item": "Toblerones","Price": 7,"Stock": 11},
        "SN4" :{"item": "Snickers","Price": 5,"Stock": 5},
        "SN5" :{"item": "M&Ms","Price": 3.50,"Stock": 6},
    }
}

#This is the function that allows the vending machine to display the menu
def display_menu():
    print("\nWelcome to the Vending Machine!\n")
    for category, items in menus.items():
        print(f"-- {category} --")
        for code, details in items.items(): #This shows the menu 
            print(f"{code}: {details['item']} - ${details['Price']} (Stock:{details['Stock']})")
        print()


#This function covers the entirety of the buying process
def purchase_item():
    while True:
        #This one asks for the users input
        code = input("Enter the code of the item you want to purchase: ").strip().upper() #This is to remove the spaces and uppercases in the input
        for category, items in menus.items():
            if code in items:
                item = items[code]
                if item['Stock'] > 0: #This is a condition where everything follows goes on the condition that there is stock
                    while True:
                        try:
                            payment = float(input(f"{item['item']} costs ${item['Price']}. Enter your payment: $"))
                            if payment >= item['Price']: #Condition where if inputted payment is equal or above the items price
                                item['Stock'] -= 1
                                change = payment - item['Price']
                                print(f"Dispensing {item['item']}... Your change is ${change:.2f}\n")
                                return
                            else: #Condition if the inputted amount is less than the price
                                print("Insufficient Amount. Try again or type x to cancel.")
                                retry = input("Enter payment or cancel: ").strip().lower()
                                if retry == 'x': #Another Condition that stops the entire process
                                    print("Transaction cancelled.\n")
                                    return
                                else:
                                    
                                    try: #Redoing the process until one of the condition or the other is met
                                        payment = float(retry) 
                                        if payment >= item['Price']:
                                            item['Stock'] -= 1
                                            change = payment - item['Price']
                                            print(f"{item['item']} dispensed... Your change is ${change:.2f}\n")
                                            return
                                        else: #
                                            print("Still insufficient amount. Try again or cancel")
                                    except ValueError:
                                        print("Invalid input. Transaction cancelled.\n")
                                        return
                        except ValueError:
                            print("Invalid input. Please enter a valid amount or x to cancel.")
                else: #This is the condition when their is no stock
                    print(f"Sorry, {item['item']} is out of stock.\n")
                return
        print("Invalid item code. Please try again.\n")




def vending_machine(): #Another function that asks if the user wants to redo the process
    while True:
        display_menu()
        purchase_item()
        while True:
            again = input("Would you like to buy another item? (y/n): ").strip().lower() #For removing the spaces and uppercases in the input
            if again in ('y', 'n'):
                break
            else:
                print("Invalid Input. Please enter a 'y' for yes or 'n' for no.")
        if again == 'n': #This input ends the entire process and shows a farewell message
            print("\nThank you for your Patronage")
            break



# Calls the vending machine function for it to start
vending_machine()


