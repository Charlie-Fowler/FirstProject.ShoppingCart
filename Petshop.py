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

print('''
Welcome to PetShop!
Please select an option from the following menu:
      
Note: in order to select an option/product,
please enter the number or name.''')

while True:
    basket = []
    basketprice = []
    print('''\n
___________________
    Menu
      
1. Add Item
2. Remove Item
3. View Basket
4. Exit 
___________________
''')
    userchoice = input('''Please select what you want to do: ''')
    print(userchoice)

    if userchoice.upper() == 'ADD ITEM' or (userchoice.isnumeric() and int(userchoice) == 1):
        for i,key in enumerate(productmenu):
            print(i,key)
        itemselection = input('Please enter the item number you would like to add: ')
        print(itemselection +' has been added to the basket')
        prod_name = products[int(itemselection)]
        basket.append(5)
        basketprice.append(productmenu[prod_name])


    elif userchoice.upper() == 'REMOVE ITEM' or (userchoice.isnumeric() and int(userchoice) == 2):
        removal = input('''Which item number would you like to remove?''' + enumerate(basket))
        basket.remove([removal])
        basketprice.remove([removal])
        print('Item Removed!')
        
    elif userchoice.upper() == 'VIEW BASKET' or (userchoice.isnumeric() and int(userchoice) == 3):
        print(basket)

    elif userchoice.upper() == 'EXIT' or (userchoice.isnumeric() and int(userchoice) == 4):
        print('Thank you for visiting us today!')
        break

    else:
        print('Invalid Choice!\nPlease try again.')

