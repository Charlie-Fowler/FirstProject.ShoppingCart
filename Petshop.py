products = ['Dog Food', 'Cat Food', 'Bone', 'Tuna Treats', 'Venison Treats',
'Flea Treatment', 'Worm Treatment', 'Scratch Post','Pet Milk']

productmenu= { 
products[0] : 24.99,
products[1] : 21.99,
products[2] : 4.00,
products[3] : 6.00,
products[4] : 5.50,
products[5] : 15.00,
products[6] : 14.50,
products[7] : 44.99,
products[8] : 2.50
}
userchoice = ''
# holding value for user choices
welcome_txt = '''
Welcome to PetShop!
Please select an option from the following menu:
      
Note: in order to select an option/product,
please enter the number or name.'''
# string variable to hold unchangable welcome
menuinterface_txt = '''\n
___________________
    Menu
      
1. Add Item
2. Remove Item
3. View Basket
4. Exit 
___________________
'''
# string variable to hold unchangable menu
basket = []
basketprice = []
# holding value for lists to hold user choices

print(welcome_txt)

#while loop always true until if choice: exit, leading to break.
while True:
    try:
        print(menuinterface_txt)
        userchoice = input('''Please select what you want to do: ''')
    # request user to select which part of menuinterface_txt they want to access
        
    # if user selects add item or 1, print productmenu dictionary, 
    # user selects by index which to add to basket
        if userchoice.upper() == 'ADD ITEM' or (userchoice.isnumeric() and int(userchoice) == 1):
            print('You have selected: Add Item\n ')
            for i,key in enumerate(productmenu):
                print(i,key)
            item_index = int(input('Please enter the item number you would like to add: '))
    # ^item index is inputted by user and converted to int to allow  index removal
            prod_name = products[item_index]
            prod_price = productmenu[prod_name]
            basket.append(prod_name)
            basketprice.append(prod_price)
            print(str(item_index) +' has been added to the basket')

    # if user choice is remove item or 2, print items in basket
        elif userchoice.upper() == 'REMOVE ITEM' or (userchoice.isnumeric() and int(userchoice) == 2):
            print('You have selected: Remove Item\n ')
            # if user has no items in the basket, prompt message
            if len(basket) == 0:
                print('You have no items in the basket!\n')
            # if items are present in basket, allow removal
            # then print basket with index's for item location for removal
        
            else:
                for i in range(len(basket)):
                    print(i, basket[i])
                # index is inputted by user, and removed from the basket and price
                item_index = int(input('Please select which item number you would like to remove: \n'))
                print('\n' + basket[item_index] +' has been removed!')
                basket.pop(item_index)
                basketprice.pop(item_index)

    # if user choice is view basket or 3, print basket with total price
        elif userchoice.upper() == 'VIEW BASKET' or (userchoice.isnumeric() and int(userchoice) == 3):
            print('''\nYou have selected: View Basket
    \nThis is what is in your basket:\n ''')
            if len(basket) == 0:
                print('You have no items in the basket!\n')
            # if items are present in basket, allow removal
            # then print basket with index's for item location for removal
        
            else:
                for i in range(len(basket)):
                    print(basket[i])
                print('''\nThe total cost is: £''' + str(sum(basketprice)))

    # if user choice is exit or 4, confirm exit and end programme
        elif userchoice.upper() == 'EXIT' or (userchoice.isnumeric() and int(userchoice) == 4):
            print('''You have selected: Exit \n
    Thank you for visiting us today!''')
            break
    # if user choice is invalid, loop will continue
        else:
            print('\nInvalid Choice!\nPlease try again.\n')
    except:
        print('\nInvalid Choice!\nPlease try again.\n')
