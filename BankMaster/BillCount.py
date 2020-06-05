print("\t\t\t***** Bill Count *****")
unit = int(input("Enter Consumed Unit : "))

ch = int(input("\n\n1.Home \n2.Industry \n3.Commercial \n\nEnter choice:"))

if ch == 1:
    home_count = unit*170
    home_bill = home_count*0.27
    print("Your Home Total Bill ", home_bill)
elif ch == 2:
    ind_count = unit * 180
    ind_bill = ind_count * 1.5
    print("Your Industry Total Bill ", ind_bill)
elif ch == 3:
    com_count = unit * 175
    com_bill = com_count * 1.2
    print("Your Commercial Total Bill ", com_bill)
else:
    print("\n\nINVALID CHOICE!")



