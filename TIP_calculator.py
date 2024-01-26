# TIP Calculator

# to calculate the tip on basis of 
# 1.total bill amount 2.Split between people 3.percentage of tip
# optional :- do round off to the nearest digit 

Bill_amount = float(input("Enter the bill amount =>"))
Tip_amount = float(input("Enter ther tip amount in percentage =>"))
Number_of_people = int(input("Enter the number of people to split between =>"))

final_amount = (Bill_amount + ((Bill_amount * Tip_amount) / 100)) / Number_of_people
final_amount = round(final_amount , 2)

print("The final amount after the adittion of TIP of {}% would be {} each".format(Tip_amount,final_amount))