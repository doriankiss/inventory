from tabulate import tabulate

#========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = int(quantity)

    def get_cost(self):  # Unused, as accessed property using dot notation
        return self.cost

    def get_quantity(self):  # Unused, as accessed property using dot notation
        return self.quantity

    # Return a string representation of the instance
    def __str__(self):
        return(f"Class: Shoe\nCountry: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\n"
            f"Quantity: {self.quantity}\n")

#=============Shoe list===========

# This list will be used to store a list of objects of shoes.
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function opens the file inventory.txt and reads the data from this file, then creates a shoes object with this data
    and appends this object into the shoes list. One line in this file represents data to create one object of shoes. It uses
    try-except for error handling. It skips the first line using code.
    '''
    with open('inventory.txt', 'r') as f:
        next(f)  # Skips first line
        for line in f:
            line_split = line.split(",")
            try:
                shoe_list.append(Shoe(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4]))
            except IndexError:
                print("IndexError")
            
def capture_shoes():
    '''
    This function allows a user to input data about a shoe and use this data to create a shoe object
    and append this object inside the shoe list (as well as append it to inventory.txt).
    '''
    # Not sure if I've understood the instructions. What does it mean to 'capture data about a shoe'?
    # Edit this to catch mistaken entries?
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = input("Cost: ")
    quantity = input("Quantity: ")
    shoe_list.append(Shoe(country, code, product, cost, quantity))

    # Save new shoe object as string to inventory.txt
    with open('inventory.txt', 'a') as f:
        f.write(f"\n{country},{code},{product},{cost},{quantity}")

def view_all():
    '''
    This function iterates over the shoes list and print the details of the in a table format
    by using Python’s tabulate module.
    '''
    pre_table = []
    for shoe in shoe_list:
        pre_array = []
        pre_array.append(shoe.country)
        pre_array.append(shoe.code)
        pre_array.append(shoe.product)
        pre_array.append(shoe.cost)
        pre_array.append(shoe.quantity)
        pre_table.append(pre_array)
    
    # Prints a graphical table from pre_table array
    print(tabulate(pre_table, headers=['Country', 'Code', 'Product', 'Cost ($)', 'Quantity'], showindex='always', tablefmt='mixed_grid'))
    input("Press <Enter> to continue. ")

def re_stock():
    '''
    This function finds the shoe object with the lowest quantity, which is the shoes that need to be re-stocked. It asks the user if they
    want to add to the quantity of shoes and then updatesit in shoe_list and inventory.txt.
    '''
    # Pre-load shoes_with_lowest_quantities with the first shoe in shoe_list
    shoes_with_lowest_quantities = [shoe_list[0]]
    # Iterate from index 1 onwards, updating shoes_with_lowest_quantities as appropriate
    for shoe in shoe_list[1:]:
        if shoe.quantity == shoes_with_lowest_quantities[0].quantity:
            shoes_with_lowest_quantities.append(shoe)
        elif shoe.quantity < shoes_with_lowest_quantities[0].quantity:
            shoes_with_lowest_quantities.clear()
            shoes_with_lowest_quantities.append(shoe)

    if len(shoes_with_lowest_quantities) == 1:
        print(f"\nThe shoe with the lowest quantity in stock is:\n\n{shoes_with_lowest_quantities[0].__str__()}")
    elif len(shoes_with_lowest_quantities) > 1:
        print("\nThe shoes with the lowest quantities in stock are:\n")
        for shoe in shoes_with_lowest_quantities:
            print(shoe.__str__())

    choice = ""
    while(choice != "yes") and (choice != "no"):
        choice = input("Would you like to restock the shoes? Enter <yes> or <no>: ").lower()
    
    if choice == "yes":
        restock_quantity = 0
        while(restock_quantity > 50) or (restock_quantity < 5):
            try:
                restock_quantity = int(input("\nHow many shoes would you like to add to the stock? Enter an integer between 5 and 50 inclusive: "))
            except ValueError:
                print("\nThat's not an integer. Please try again. ")
                input("Press <Enter> to continue. ")
                continue
        # restock lowest quantity shoe(s) with specified quantity
        for shoe in shoes_with_lowest_quantities:
            shoe.quantity += restock_quantity

        # Overwrite inventory.txt with updated shoe_list
        with open('inventory.txt', 'w') as f:
            f.write("Country,Code,Product,Cost,Quantity")
            for shoe in shoe_list:
                f.write(f'\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}')
        
        # Print update:
        if len(shoes_with_lowest_quantities) == 1:
            print(f"\nItem restocked successfully:\n\n{shoes_with_lowest_quantities[0].__str__()}")
        elif len(shoes_with_lowest_quantities) > 1:
            print("\nItems restocked successfully:\n")
            for shoe in shoes_with_lowest_quantities:
                print(shoe.__str__())
        input("Press <Enter> to continue. ")

    elif choice == "no":
        pass  

def seach_shoe():
    '''
     This function searches for a shoe from the list using the shoe code and prints this object.
    '''
    # Take in string, convert to upper-case and remove surrounding whitespace
    search_code = input("\nEnter the code of the shoe you're looking for: ").upper().strip()
    
    num_found = 0
    for shoe in shoe_list:
        if shoe.code == search_code:
            print("\nThis shoe matches the code you entered:\n")
            print(shoe.__str__())
            num_found +=1
    if num_found == 0:
        print("No shoes were found with that code. ")
    
    input("Press <Enter> to continue. ")

def value_per_item():
    '''
    This function calculates the total value for each item and prints this information on the console for all of the shoes.
    '''
    pre_table = []
    for shoe in shoe_list:
        pre_array = []
        pre_array.append(shoe.country)
        pre_array.append(shoe.code)
        pre_array.append(shoe.product)
        pre_array.append(shoe.cost)
        pre_array.append(shoe.quantity)
        pre_array.append(int(shoe.cost) * int(shoe.quantity))
        pre_table.append(pre_array)
    
    # Prints a graphical table from pre_table array
    print(tabulate(pre_table, headers=['Country', 'Code', 'Product', 'Cost ($)', 'Quantity', 'Total Value ($)'], showindex='always', tablefmt='mixed_grid'))
    input("Press <Enter> to continue. ")

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being on sale.
    '''
    shoes_with_highest_quantities = [shoe_list[0]]

    for shoe in shoe_list[1:]:
        if shoe.quantity == shoes_with_highest_quantities[0].quantity:
            shoes_with_highest_quantities.append(shoe)
        elif shoe.quantity > shoes_with_highest_quantities[0].quantity:
            shoes_with_highest_quantities.clear()
            shoes_with_highest_quantities.append(shoe)

    if len(shoes_with_highest_quantities) == 1:
        print(f"\nThe shoe with the highest quantity in stock is:\n\n{shoes_with_highest_quantities[0].__str__()}")
        print("This shoe is on SALE!")
    elif len(shoes_with_highest_quantities) > 1:
        print("\nThe shoes with the highest quantities in stock are:\n")
        for shoe in shoes_with_highest_quantities:
            print(shoe.__str__())
        print("These shoes are on SALE!")
    
    input("Press <Enter> to continue. ")

# Populate shoe_list:
read_shoes_data()

#==========Main Menu=============
'''
Mnu that executes each function above.
'''
while True:
    choice = input("\nMain menu\n"
                    "<1> - View all shoes in stock\n"
                    "<2> - Restock\n"
                    "<3> - View total value per item\n"
                    "<4> - Search shoe by code\n"
                    "<5> - See the shoe(s) with the highest quantities\n"
                    "<6> - Add a new shoe item to the stock\n"
                    "<7> - Exit program\n"
                    "Enter the number corresponding to your choice: ")

    if choice == "1":
        view_all()
    elif choice == "2":
        re_stock()
    elif choice == "3":
        value_per_item()
    elif choice == "4":
        seach_shoe()
    elif choice == "5":
        highest_qty()
    elif choice == "6":
        capture_shoes()
    elif choice == "7":
        exit()
    else:
        continue

