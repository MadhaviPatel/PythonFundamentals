print("\t\t\t***** Bill Count *****")
unit = int(input("Enter Consumed Unit : "))

ch = int(input("\n\n1.Home \n2.Industry \n3.Commercial \n\nEnter choice:"))
fixed_charge = 50

if ch == 1:
    home_count1 = 0
    home_count2 = 0
    home_count3 = 0
    fixed_charge = 50
    fuel_charge = unit * 1.98
    if unit >= 50:
        unit = unit - 50
        home_count1 = 50 * 3.2
        if unit >= 150:
            unit = unit - 150
            home_count2 = 150 * 3.9
            if unit >= 0:
                home_count3 = 150 * 4.5
        else:
            home_count2 = 150 * 3.9
    else:
        home_count1 = unit * 3.2
    charge = home_count1 + home_count2
    home = charge + fuel_charge + fixed_charge
    tax = home * 0.15
    bill = home + tax
    print("Your Home Total Bill ", bill)
    print("your electricity ", charge)
    print("bill with govt tax ", tax)
elif ch == 2:
    ind_count = unit * 4.50
    fuel_charge = unit * 1.98
    ind = ind_count + fuel_charge + fixed_charge
    tax = ind * 0.10
    bill = tax + ind
    print("Your Industry Total Bill ", bill)
    print("your electricity ", ind_count)
    print("bill with govt tax ", tax)
elif ch == 3:
    com_count = unit * 4.50
    fuel_charge = unit * 1.98
    com = com_count + fuel_charge + fixed_charge
    tax = com * 0.10
    bill = tax + com
    print("Your Commercial Total Bill ", bill)
    print("your electricity ", com_count)
    print("bill with govt tax ", tax)
else:
    print("\n\nINVALID CHOICE!")
