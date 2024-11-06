# Restaurant_orders

food_menu = {
    'gyro chicken' : {
        'cost per order' : 6.25,
        'price per order': 7.50,
    },
    'gyro vegan' : 
        {
        'cost per order' : 6.15, 
        'price per order': 8.25,
        }
}

drinks_menu = {
    'water' : {
        'cost per order':0.25,
        'price per order':0.00,
    },
    'soda': {
        'cost per order':0.50,
        'price per order':1.50,
    },
}


total_profit = 0

#creating a function to get user input and validate
def validate_user_input(user_input, meal):
    if len(user_input) < 1:
        print('Error message, provide an input')
        return 'error'
    else:
        try:
            user_input = float(user_input)
            if user_input < 0:
                 print("Error: Please enter a value greater than 0")
                 return 'error'
            else:
                print("Error: Please enter a valid string, not a number.")
                return 'error'
        except ValueError:
            if meal == 'food':
                for key in food_menu:
                    if user_input.lower() == key.lower():
                        return user_input
                print('\nThis is not available')
                for key in food_menu:
                    print(key)
            if meal == 'drinks':
                for key in drinks_menu:
                    if user_input.lower() == key.lower():
                        return user_input
                print('\nThis is not available')
                for key in drinks_menu:
                    print(key)
            return 'error'
            



#function to collect orders
def collect_order():
    global total_profit
    print('\nSelect what food you want')
    for key in food_menu:
        print(key +' ' + str(food_menu[key]['price per order']))
        
    #get user input
    user_input = 'error'
    while user_input == 'error':
       user_input = validate_user_input(input('Enter your meal selection'), 'food') 
    

    print('Select what drink you want')
    for key in drinks_menu:
        print(key +' ' + str(drinks_menu[key]['price per order']))
        
    drink_input = 'error'
    while drink_input == 'error':
       drink_input = validate_user_input(input('Enter your drink selection'), 'drinks') 

    for key in food_menu:
        if user_input.lower() == key.lower():
            a = user_input.title()
    for key in drinks_menu:
        if drink_input.lower() == key.lower():
            b = drink_input.title()

    #to display price of the meal and the meal ordered
    meal_price = food_menu[user_input]['price per order'] 
    meal_cost = food_menu[user_input]['cost per order']
    drink_price = drinks_menu[drink_input]['price per order']
    drink_cost = drinks_menu[drink_input]['cost per order']
    total_price = meal_price + drink_price
    print('Your order is ' + a + ' and ' +b)
    print('The price of your food is £' + str(total_price))
    profit = (meal_price - meal_cost) + (drink_price - drink_cost)
    total_profit += profit


#defining a function to collect orders
def restaurant_order(orders):
    global total_profit
    #to run the order three times
    for numbers in range(orders):
        print('\nProvide your order ' + str(numbers + 1))
        collect_order()
    print('\nThe Total Profit made is £' + str(round(total_profit,2)))

restaurant_order(3)
