items = {
    'itemA': {
        'category': 'ICE-CREAM',
        'name': 'KWALITY',
        'code': 100,
        'price': 5.00,
        'stock': 11
    },
    'itemB': {
        'category': 'CHIPS',
        'name': 'LAYS',
        'code': 101,
        'price': 4,
        'stock': 21
    },
    'itemC': {
        'category': 'BEVERAGES',
        'name': 'LEMON Punch',
        'code': 102,
        'price': 10,
        'stock': 14
    },
    
    
}


print("Category:", items['itemA']['category'])
print("Name:", items['itemA']['name'])
print("Code:", items['itemA']['code'])
print("Price:", items['itemA']['price'])
print("Stock:", items['itemA']['stock'])

print("Category:", items['itemB']['category'])
print("Name:", items['itemB']['name'])
print("Code:", items['itemB']['code'])
print("Price:", items['itemB']['price'])
print("Stock:", items['itemB']['stock']) 

print("Category:", items['itemC']['category'])
print("Name:", items['itemC']['name'])
print("Code:", items['itemC']['code'])
print("Price:", items['itemC']['price'])
print("Stock:", items['itemC']['stock'])

print("Please select an item:")
for key, item in items.items():
    print(f"{key}. {item['name']} - Dhs {item['price']}")

SELECTION = input("Enter the item no. you wish for...")

if SELECTION in items:
    SELECTION_item = items [SELECTION]
    print ("Your item is {SELECTION_item['name']}.")
    AMOUNT_PAID = SELECTION_item['price']

    while AMOUNT_PAID > 0:
        try:
            pay = float(input(f"Please insert Dhs {AMOUNT_PAID:.2f}: "))
            if pay >= AMOUNT_PAID:
                balance = pay - AMOUNT_PAID
                print(f"Thank you for purchasing! Your balance is ${balance:.2f}.")
                break
            else:
                print("Insufficient pay. Please insert more money.")
                AMOUNT_PAID -= pay
        except ValueError:
            print("Invalid pay amount. Please enter a valid number.")
else:
    print("Invalid selection. Please try again.")