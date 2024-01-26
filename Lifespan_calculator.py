# life calculator

# a person has 4,680 weeks in his life
# calculate the weeks a person has left on the basis of his/her age

total_number_of_weeks = 4680
current_age = float(input("Enter your curent age =>"))

weeks_left = total_number_of_weeks - ( current_age * 52)
weeks_left = int(weeks_left)

print(f"You have {weeks_left} weeks left in your life (average)")
